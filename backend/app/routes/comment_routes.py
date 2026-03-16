from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.database import SessionLocal
from models.comment_model import TaskComment
from models.task_model import Task
from schema.comment_schema import CommentCreate, CommentResponse

router = APIRouter(prefix="/comment",tags=["Task Comment"])

# DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create Comment 
@router.post("/{task_id}/comments", response_model=CommentResponse)
def add_comment(task_id: int, comment: CommentCreate, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    new_comment = TaskComment(
        task_id=task_id,
        comment=comment.comment,
        commented_by=comment.commented_by
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment

# Get all comments of a task [GET]:
@router.get("/{task_id}/comments", response_model=list[CommentResponse])
def get_comments(task_id: int, db: Session = Depends(get_db)):

    comments = db.query(TaskComment).filter(TaskComment.task_id == task_id).all()

    return comments

# @router.delete("/comments/{comment_id}")
# def delete_comment(comment_id: int, db: Session = Depends(get_db)):

#     comment = db.query(TaskComment).filter(TaskComment.id == comment_id).first()

#     if not comment:
#         raise HTTPException(status_code=404, detail="Comment not found")

#     db.delete(comment)
#     db.commit()

#     return {"message": "Comment deleted successfully"}

