from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session

from models.project_model import Project
from schema.project_schema import ProjectCreate,ProjectResponse,ProjectUpdate
from config.database import SessionLocal

router = APIRouter(prefix="/projects", tags=["Projects"])

# DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create project [POST]:
@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):

    new_project = Project(
        name=project.name,
        description=project.description,
        created_by=project.created_by
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

# fetch project [GET]:
@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):

    projects = db.query(Project).all()
    return projects

# fetch project by id [GET]/id:
@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

# modify project [PUT]:
@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if data.name:
        project.name = data.name

    if data.description:
        project.description = data.description

    db.commit()
    db.refresh(project)

    return project

# delete project [DELETE]:
@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):

    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}