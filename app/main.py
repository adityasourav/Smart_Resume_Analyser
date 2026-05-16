from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Smart Resume Analyzer"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Smart Resume Analyzer Running"
    }