import pdfplumber
import re
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "fastapi",
    "django",
    "machine learning",
    "tensorflow",
    "react",
    "docker",
    "aws"
]


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text


def extract_email(text):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    matches = re.findall(pattern, text)

    return matches[0] if matches else "Not Found"


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return "Not Found"


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def parse_resume(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text)
    }

    return data