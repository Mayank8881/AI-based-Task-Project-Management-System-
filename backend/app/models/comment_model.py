from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.database import Base

class TaskComment(Base):
    __tablename__="task_comments"

    id = Column(Integer,primary_key=True,index=True)
    task_id=Column(Integer,ForeignKey("tasks.id"),nullable=False)
    comment=Column(Text,nullable=False)
    commented_by=Column(String(255))
    created_at=Column(TIMESTAMP, server_default=func.now())

    tasks = relationship("Task", back_populates="comments")