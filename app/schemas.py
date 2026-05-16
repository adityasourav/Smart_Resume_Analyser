from pydantic import BaseModel

class ResumeResponse(BaseModel):
    name: str
    email: str
    skills: list
    score: int

    class Config:
        orm_mode = True