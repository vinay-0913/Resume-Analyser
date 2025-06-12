from keybert import KeyBERT
from rapidfuzz import fuzz

# Initialize model once
kw_model = KeyBERT()

def extract_keywords(text, top_n=10):
    """
    Extracts top keywords from the job description using KeyBERT.
    """
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words='english',
        top_n=top_n
    )
    return [kw[0] for kw in keywords]

def match_keywords(keywords, resume_text, threshold=80):
    """
    Matches extracted keywords against resume text (case-insensitive).
    """
    resume_text = resume_text.lower()
    matched = []

    for kw in keywords:
        kw_clean = kw.lower().strip()
        # Direct match first
        if kw_clean in resume_text:
            matched.append(kw)
        else:
            # Fuzzy match with partial ratio
            score = fuzz.partial_ratio(kw_clean, resume_text)
            if score >= threshold:
                matched.append(kw)

    return matched