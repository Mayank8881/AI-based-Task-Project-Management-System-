from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    project_id: int
    title: str
    assignee: Optional[str] = None
    created_by: Optional[str] = None


class TaskResponse(BaseModel):
    id: int
    project_id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    assignee: Optional[str]
    created_by: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None
    assignee: str | None = None

class TaskStatusUpdate(BaseModel):
    status: str