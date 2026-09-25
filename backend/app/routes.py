from fastapi import APIRouter, File, UploadFile

from app.pdf_utils import extract_text_from_pdf
from app.retrieval import retrieve_answer

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)

    return {
        "filename": file.filename,
        "text": text,
    }


@router.post("/ask")
async def ask_question(question: str, text: str):
    result = retrieve_answer(question, text)
    return result