# Resume Analyser
This is a **Resume Analyser** that analyzes resumes against job descriptions using NLP techniques.It extracts and compares keywords, skills, and job titles, calculates semantic similarity with Sentence-BERT, and provides an ATS compatibility check. The system generates a match score out of 100 and offers personalized suggestions to improve resume score.


![Website Screenshot](./frontend/public/Screenshot1.png)

![Website Screenshot](./frontend/public/Screenshot3.png)

![Website Screenshot](./frontend/public/Screenshot2.png)

## 🔧 Tech Stack

- **Frontend**: React.js with Tailwind CSS for styling, Lucide React for icons, and Context API for state management.

- **Backend**: Flask (Python) for resume analysis APIs using NLP techniques.

- **Resume Analysis Engine**:

  - **Text Extraction**: `fitz` (PyMuPDF) for PDF files, `docx` for DOCX parsing.

  - **NLP & Similarity**:
    - `nltk`: tokenization, lemmatization, and stopword removal.
    - `keybert`: keyword extraction.
    - `sentence-transformers` (Sentence-BERT): semantic similarity.
    - `rapidfuzz`: fast string matching.
    - `spacy`: Named Entity Recognition (NER).





