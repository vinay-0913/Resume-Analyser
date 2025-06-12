import os
import fitz  # PyMuPDF
import docx

def extract_text_from_file(file_path):
    try:
        ext = os.path.splitext(file_path)[1].lower()

        if ext == '.pdf':
            return extract_text_from_pdf(file_path)
        elif ext == '.docx':
            return extract_text_from_docx(file_path)
        else:
            return f"Unsupported file format: {ext}"

    except Exception as e:
        return f"Error extracting text: {str(e)}"

def extract_text_from_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

