# Smart Resume Analyzer

An AI-powered resume analysis system built using FastAPI and NLP techniques.

## Features

- Resume PDF Upload
- Resume Parsing
- Skill Extraction
- Job Description Matching
- Match Score Generation
- NLP-based Similarity Analysis

## Tech Stack

- Python
- FastAPI
- spaCy
- scikit-learn
- TF-IDF
- Cosine Similarity
- PyMuPDF / pdfplumber

## Project Structure

```text
Smart_Resume_Analyser/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── resume_parser.py
│   ├── jd_matcher.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
│
├── uploads/
├── README.md
└── .gitignore
```
## Installation

```bash
pip install -r requirements.txt
