from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import call_openrouter

class TitleInput(BaseModel):
    title: str


class TaskInput(BaseModel):
    title: str
    description: str

router = APIRouter(prefix="/ai", tags=["AI Features"])


@router.post("/generate-description")
def generate_description(data: TitleInput):

    prompt = f"""
    Generate a clear and detailed task description for the following task title:

    Title: {data.title}

    The description should explain the work required.

    Only generate the descriptinon in plain text 
    word limit 40-50 words.
    """

    description = call_openrouter(prompt)

    return {
        "title": data.title,
        "generated_description": description
    }



@router.post("/suggest-priority")
def suggest_priority(data: TaskInput):

    prompt = f"""
    Analyze the following task and suggest a priority level.

    Title: {data.title}
    Description: {data.description}

    Priority must be one of:
    Low
    Medium
    High

    Only return the priority.
    """

    priority = call_openrouter(prompt)

    return {
        "suggested_priority": priority.strip()
    }