from app.data.skills_list import *

def extract_known_skills(text):
    text_lower = text.lower()

    return {
        "hard_skills": [s for s in HARD_SKILLS if s.lower() in text_lower],
        "soft_skills": [s for s in SOFT_SKILLS if s.lower() in text_lower],
        "tools": [s for s in TOOLS_CERTS if s.lower() in text_lower],
        "job_titles": [s for s in JOB_TITLES if s.lower() in text_lower],
        "education": [s for s in EDUCATION_TERMS if s.lower() in text_lower]
    }
