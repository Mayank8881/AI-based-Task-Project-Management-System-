from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CommentCreate(BaseModel):
    comment: str
    commented_by: Optional[str] = None


class CommentResponse(BaseModel):
    id: int
    task_id: int
    comment: str
    commented_by: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True