from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    created_by: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    created_by: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None