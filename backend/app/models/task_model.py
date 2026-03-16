from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    title = Column(String(50), nullable=False)
    description = Column(Text)

    status = Column(String(20), default="todo")
    priority = Column(String(20))

    assignee = Column(String(20))
    created_by = Column(String(20))

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())

    projects = relationship("Project", back_populates="tasks")
    comments = relationship("TaskComment", back_populates="tasks", cascade="all, delete")