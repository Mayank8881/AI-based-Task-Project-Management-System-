from fastapi import FastAPI
from config.database import engine
from sqlalchemy import text

from models import project_model
from models import comment_model
from models import task_model

from routes import project_routes
from routes import task_routes
from routes import comment_routes
from routes import ai_routes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Project Management API",
    version="1.0.0"
)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check for database connection.
# @app.on_event("startup")
# def check_database_connection():
#     try:
#         with engine.connect() as connection:
#             connection.execute(text("SELECT 1"))
#         print("Database connected successfully")
#     except Exception as e:
#         print("Database connection failed")
#         print(e)


@app.get("/")
def home():
    return {"message": "AI Project Task Management API Running"}

app.include_router(project_routes.router)
app.include_router(task_routes.router)
app.include_router(comment_routes.router)
app.include_router(ai_routes.router)