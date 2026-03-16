from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from config.database import SessionLocal
from models.task_model import Task
from models.project_model import Project
from schema.task_schema import TaskCreate, TaskResponse,TaskUpdate ,TaskStatusUpdate
from services.ai_service import generate_task_details
import json

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create tasks [POST]:

# @router.post("/",response_model=TaskResponse)
# def createtask(task:TaskCreate,db:Session=Depends(get_db)):
    
#     project = db.query(Project).filter(Project.id == task.project_id).first()

#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found")
    
#     new_task=Task(
#         project_id=task.project_id,
#         title=task.title,
#         description=task.description,
#         status=task.status,
#         priority=task.priority,
#         assignee=task.assignee,
#         created_by=task.created_by
#     )

#     db.add(new_task)
#     db.commit()
#     db.refresh(new_task)

#     return new_task

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == task.project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Step 1 — create base task
    new_task = Task(
        project_id=task.project_id,
        title=task.title,
        assignee=task.assignee,
        created_by=task.created_by,
        status="todo",
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    # Step 2 — AI generation
    try:

        ai_result = generate_task_details(task.title)

        print("AI RESULT:", ai_result)

        cleaned = ai_result.replace("```json", "").replace("```", "").strip()

        ai_data = json.loads(cleaned)

        new_task.description = ai_data.get("description", "")
        new_task.priority = ai_data.get("priority", "").lower()

        db.commit()
        db.refresh(new_task)

    except Exception as e:

        print("AI ERROR:", e)

        new_task.description = "AI description generation failed"
        new_task.priority = ""

        db.commit()
        db.refresh(new_task)

    return new_task


# fetch task[GET]:
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    status: str | None = Query(None),
    priority: str | None = Query(None),
    assignee: str | None = Query(None),
    db: Session = Depends(get_db)
):

    query = db.query(Task)

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    if assignee:
        query = query.filter(Task.assignee == assignee)

    tasks = query.all()

    return tasks


# fetch task by id [GET]/id:
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# upadte task [PUT]:
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if data.title:
        task.title = data.title

    if data.description:
        task.description = data.description

    if data.status:
        task.status = data.status

    if data.priority:
        task.priority = data.priority

    if data.assignee:
        task.assignee = data.assignee

    db.commit()
    db.refresh(task)

    return task


# delete task [DELETE]:
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}

# get task by project 
@router.get("/project/{project_id}", response_model=list[TaskResponse])
def get_tasks_by_project(project_id: int, db: Session = Depends(get_db)):

    tasks = db.query(Task).filter(Task.project_id == project_id).all()

    return tasks

# partical update on status
@router.patch("/{task_id}/status")
def update_task_status(task_id: int, data: TaskStatusUpdate, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = data.status

    db.commit()
    db.refresh(task)

    return {
        "message": "Task status updated",
        "task": task
    }