from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from config.database import Base
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    created_by = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())

    tasks = relationship("Task", back_populates="projects", cascade="all, delete")