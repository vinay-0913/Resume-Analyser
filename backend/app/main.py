from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import tempfile
import os
from app.keyword_utils import extract_keywords, match_keywords
from app.utils.text_extractor import extract_text_from_file
from app.utils.skill_matcher import extract_known_skills
from app.utils.ner_extractor import extract_named_entities
from app.utils.semantic_matcher import get_semantic_matches
from app.utils.ats_checker import check_section_headings, check_date_format
from app.utils.recommender import generate_recommendations
from app.utils.scorer import calculate_score



main = Blueprint('main', __name__)

@main.route('/analyze', methods=['POST'])
def analyze_resume():
    if 'resume' not in request.files or 'job_description' not in request.form:
        return jsonify({"error": "Missing resume or job description"}), 400

    resume_file = request.files['resume']
    job_description = request.form['job_description']
    
    # Step 1: Extract keyphrases from JD
    keywords = extract_keywords(job_description)

    # Step 2: Extract resume text + Run ATS checks
    filename = secure_filename(resume_file.filename)
    ext = os.path.splitext(filename)[1]

    with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
        resume_file.save(tmp.name)
        resume_text = extract_text_from_file(tmp.name)

    os.remove(tmp.name)

    ats_headings = check_section_headings(resume_text)
    ats_dates = check_date_format(resume_text)
    

    # Step 3: Keyword Matching
    matched_keywords = match_keywords(keywords, resume_text)

    # Step 4: Skill Extraction
    resume_skills = extract_known_skills(resume_text)
    jd_skills = extract_known_skills(job_description)

    matched_skills = {
        key: list(set(resume_skills[key]) & set(jd_skills[key]))
        for key in resume_skills
    }
    recommendations = generate_recommendations(
    resume_skills=resume_skills,
    jd_skills=jd_skills,
    matched_skills=matched_skills,
    matched_keywords=matched_keywords
    )

    # ✅ Step 5: Missing Skills Suggestions
    missing_skills = {
        key: list(set(jd_skills.get(key, [])) - set(resume_skills.get(key, [])))
        for key in jd_skills
    }

    # Step 6: Named Entity Recognition
    resume_entities = extract_named_entities(resume_text)
    jd_entities = extract_named_entities(job_description)

    # After extracting keywords & resume_text
    semantic_matches = get_semantic_matches(keywords, resume_text)

    #Final Score
    score_out_of_100, score_summary = calculate_score(resume_skills, jd_skills, matched_skills, semantic_matches)


    print(f"📄 Received file: {resume_file.filename}")
    print(f"📄 Job Description received. Length: {len(job_description)} characters")


    return jsonify({
        "ats_compatibility": {"section_headings": ats_headings,
        "date_format_check": ats_dates},
        "keywords": keywords,
        "matched_keywords": matched_keywords,
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_entities": resume_entities,
        "jd_entities": jd_entities,
        "semantic_matches": semantic_matches,
        "score_summary": score_summary,
        "score_out_of_100": score_out_of_100,
        "recommendations": recommendations
    }), 200
