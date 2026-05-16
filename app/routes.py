from fastapi import APIRouter, UploadFile, File
import shutil

from app.resume_parser import parse_resume
from app.jd_matcher import calculate_match
from app.resume_parser import extract_text_from_pdf

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    parsed_data = parse_resume(file_path)

    return {
        "message": "Resume uploaded successfully",
        "data": parsed_data
    }


@router.post("/match-job")
async def match_job(file: UploadFile = File(...), jd: str = ""):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    score = calculate_match(resume_text, jd)

    return {
        "match_score": score
    }