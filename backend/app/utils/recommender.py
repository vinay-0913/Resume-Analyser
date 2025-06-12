def generate_recommendations(resume_skills, jd_skills, matched_skills, matched_keywords):
    tips = []

    # ✅ Suggest adding missing job titles
    missing_titles = set(jd_skills.get("job_titles", [])) - set(resume_skills.get("job_titles", []))
    for title in missing_titles:
        tips.append(f"Add '{title}' to your resume title or experience section.")

    # ✅ Recommend missing soft skills
    missing_soft = set(jd_skills.get("soft_skills", [])) - set(resume_skills.get("soft_skills", []))
    for skill in missing_soft:
        tips.append(f"Mention '{skill}' explicitly in your resume.")

    # ✅ Recommend missing hard skills
    missing_hard = set(jd_skills.get("hard_skills", [])) - set(resume_skills.get("hard_skills", []))
    for skill in missing_hard:
        tips.append(f"Consider highlighting '{skill}' in your resume projects or skills section.")

    # ✅ Recommend missing tools
    missing_tools = set(jd_skills.get("tools", [])) - set(resume_skills.get("tools", []))
    for tool in missing_tools:
        tips.append(f"Add familiarity with '{tool}' if you have experience using it.")

    # ✅ Bonus: Low keyword match = suggest more alignment
    if len(matched_keywords) < 3:
        tips.append("Try to align your resume wording more closely with the job description keywords.")

    # ✅ Bonus: No job title match
    if not matched_skills.get("job_titles"):
        tips.append("Ensure your job title or role matches the position you're applying for.")

    return tips
