def calculate_score(resume_skills, jd_skills, matched_skills, semantic_matches):
    total = {
        "hard_skill": len(jd_skills.get("hard_skills", [])),
        "soft_skill": len(jd_skills.get("soft_skills", [])),
        "tools": len(jd_skills.get("tools", [])),
        "job_titles": len(jd_skills.get("job_titles", [])),
        "semantic": 1  # always expect 1 or 0 semantic match
    }

    score = {
        "hard_skill": len(matched_skills.get("hard_skills", [])),
        "soft_skill": len(matched_skills.get("soft_skills", [])),
        "tools": len(matched_skills.get("tools", [])),
        "job_titles": len(matched_skills.get("job_titles", [])),
        "semantic": 1 if semantic_matches else 0
    }

    # Scoring weights
    weights = {
        "hard_skill": 30,
        "soft_skill": 15,
        "tools": 15,
        "job_titles": 10,
        "semantic": 30
    }

    # Calculate weighted score
    total_score = 0
    for key in weights:
        possible = total[key] if total[key] > 0 else 1  # avoid divide by 0
        matched = score[key]
        ratio = matched / possible
        total_score += ratio * weights[key]

    score_summary = {
        "hard_skill_match": f"{score['hard_skill']} / {total['hard_skill']}",
        "soft_skill_match": f"{score['soft_skill']} / {total['soft_skill']}",
        "tool_match": f"{score['tools']} / {total['tools']}",
        "job_title_match": f"{score['job_titles']} / {total['job_titles']}",
        "semantic_match": f"{score['semantic']} / {total['semantic']}"
    }

    return round(total_score), score_summary
