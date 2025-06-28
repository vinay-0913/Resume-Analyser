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

## Features

  - Match resumes with job descriptions using NLP.
  - Extract hard skills, soft skills, tools, and job titles.
  - Semantic similarity scoring with Sentence-BERT.
  - ATS compatibility checks (tables, columns, sections).
  - Resume match score with detailed breakdown.
  - Personalized improvement suggestions.

## 🖥️ Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vinay-0913/News-Aggregator-with-Recommendation-System.git
    ```
2. **Install dependencies**:
   - Navigate to the frontend directory and run:
    ```bash
    npm install
    ```
    - Navigate to the backend directory and run:
    ```bash
    pip install -r requirements.txt
    ```
3. **Create Python Virual Environment**:    
   - In root directory run :
    ```bash
    python -m venv env
    ```
    - Then activate it : 
    ```bash
    .venv\Scripts\activate
    ```
4. **Start the development server**:
   - Run the backend server:
    ```bash
    python run.py
    ```
   - Run the frontend server:
    ```bash
    npm start
    ```   
