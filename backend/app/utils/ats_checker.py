import re
import fitz  # PyMuPDF

def check_section_headings(text):
    expected = {
        "summary" : ["professional summary", "summary"],
        "education": ["education", "academic background"],
        "experience": ["experience", "work experience", "professional experience"],
        "skills": ["skills", "technical skills"],
        "projects": ["projects", "project work"],
        "certifications": ["certifications", "licenses", "certificates"],
    }

    # Normalize extracted lines
    lines = [re.sub(r"[^a-zA-Z ]", "", line).strip().lower() for line in text.split("\n") if line.strip()]
    
    found = []
    for key, variations in expected.items():
        if any(variant in lines for variant in variations):
            found.append(key)

    missing = [key for key in expected if key not in found]

    return {"found": found, "missing": missing}


def check_date_format(text):
    # Simple regex for date ranges
    pattern = r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s?\d{4}"
    matches = re.findall(pattern, text)
    return {"date_formats_found": matches, "is_consistent": len(matches) >= 2}

