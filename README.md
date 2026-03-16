# AI-Assisted Mini Project Management Tool

## Overview

The **AI-Assisted Mini Project Management Tool** is a lightweight full-stack web application designed to help teams manage projects and tasks efficiently. The application allows users to create projects, add tasks, track task progress, assign team members, and collaborate through task comments.

A key highlight of this system is the **AI integration**, which automatically generates task descriptions and suggests task priorities based on the task title using a **Large Language Model via the OpenRouter API**.

The backend is built with **FastAPI and PostgreSQL**, while the frontend is built using **Angular with Signals and TailwindCSS**. The project demonstrates how AI can enhance traditional project management workflows by automating repetitive tasks.

---

# Features

## Project Management
- Create new projects
- View all projects
- Update project information
- Delete projects

## Task Management
- Create tasks under projects
- Assign tasks to team members
- Track task status
- Update task status dynamically
- Delete tasks

## AI-Generated Task Details
When a task is created:
- AI generates a **task description**
- AI suggests **task priority (Low / Medium / High)**

This helps reduce manual effort and ensures tasks have meaningful descriptions.

## Task Filtering
Tasks can be filtered using:
- Project
- Priority
- Status
- Assignee

## Task Status Management
Tasks can move between:
- Todo
- In Progress
- Done

Status updates are handled using a **PATCH API endpoint**.

## Comment System
- Add comments to tasks
- View comments for each task
- Lazy load comments to improve performance

## UI Enhancements
- Modal-based task creation
- Colored status badges
- Colored priority badges
- Lazy loaded comments
- Modern responsive UI

---

# Tech Stack

## Backend

| Technology | Purpose |
|------------|--------|
| FastAPI | Backend API framework |
| SQLAlchemy | ORM for database interaction |
| PostgreSQL | Relational database |
| Pydantic | Request validation |
| OpenRouter API | AI model provider |

---

## Frontend

| Technology | Purpose |
|------------|--------|
| Angular (Latest) | Frontend framework |
| Angular Signals | State management |
| TailwindCSS | Styling |
| Standalone Components | Modular UI components |

---

# Project Structure
```bash
project-root
│
├── backend
│ │
│ ├── app
│ │ │
│ │ ├── config
│ │ │ └── database.py
│ │ │
│ │ ├── models
│ │ │ ├── project_model.py
│ │ │ ├── task_model.py
│ │ │ └── comment_model.py
│ │ │
│ │ ├── schemas
│ │ │ ├── project_schema.py
│ │ │ ├── task_schema.py
│ │ │ └── comment_schema.py
│ │ │
│ │ ├── routes
│ │ │ ├── project_routes.py
│ │ │ ├── task_routes.py
│ │ │ └── comment_routes.py
│ │ │
│ │ ├── services
│ │ │ └── ai_service.py
│ │ │
│ │ └── main.py
│ │
│ └── requirements.txt
│
└── frontend
│
└── src
│
└── app
│
├── services
│ └── api.service.ts
│
├── pages
│ ├── tasks
│ │ ├── tasks.ts
│ │ ├── tasks.html
│ │ └── tasks.css
│ │
│ └── projects
│
├── components
│ ├── task-form
│ │ ├── task-form.ts
│ │ └── task-form.html
│ │
│ ├── project-form
│ │ ├── project-form.ts
│ │ └── project-form.html
│ │
│ └── comment-box
│ ├── comment-box.ts
│ └── comment-box.html
│
└── app.config.ts
```

---

# Database Schema

## Projects Table

| Column | Type | Description |
|------|------|-------------|
| id | serial (PK) | Project ID |
| name | text | Project name |
| description | text | Project description |
| created_by | text | Creator |
| created_at | timestamp | Created time |

---

## Tasks Table

| Column | Type | Description |
|------|------|-------------|
| id | serial (PK) | Task ID |
| project_id | integer (FK) | Project reference |
| title | text | Task title |
| description | text | Task description |
| status | text | Task status |
| priority | text | Task priority |
| assignee | text | Assigned user |
| created_by | text | Creator |
| created_at | timestamp | Created time |
| updated_at | timestamp | Last updated |

---

## Task Comments Table

| Column | Type | Description |
|------|------|-------------|
| id | serial (PK) | Comment ID |
| task_id | integer (FK) | Task reference |
| comment | text | Comment content |
| commented_by | text | Comment author |
| created_at | timestamp | Created time |

# Relationships
```bash
1 Project → Many Tasks
1 Task → Many Comments
```


---

# API Endpoints

## Project APIs

| Method | Endpoint | Description |
|------|------|-------------|
| POST | /projects | Create project |
| GET | /projects | Get all projects |
| GET | /projects/{id} | Get project |
| PUT | /projects/{id} | Update project |
| DELETE | /projects/{id} | Delete project |

---

## Task APIs

| Method | Endpoint | Description |
|------|------|-------------|
| POST | /tasks | Create task |
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task |
| GET | /tasks/project/{project_id} | Tasks by project |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |
| PATCH | /tasks/{id}/status | Update task status |

---

## Comment APIs

| Method | Endpoint | Description |
|------|------|-------------|
| POST | /comment/{task_id}/comments | Add comment |
| GET | /comment/{task_id}/comments | Get comments |

---

# AI Task Generation Flow
```bash
User Creates Task
↓
FastAPI Endpoint
↓
Save Task Title
↓
Call OpenRouter API
↓
Generate Description + Priority
↓
Update Task Record
↓
Return Response
```



---

# Installation and Setup

## Backend Setup

### Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2 python-dotenv requests

```
# Environment Variables
```bash

OPENROUTER_API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost/dbname
```

# Run Backend

```bash
uvicorn app.main:app --reload
```

## Backend URL
```bash
http://localhost:8000
```
## Swagger UI
```bash
http://localhost:8000/docs
```

# Run Frontend
## Install Dependencies
```bash
npm install
```

## Run Angular Application
```bash
ng start 
```

## Frontend URL
```bash
http://localhost:4200
```

# Author
MAYANK MOKHERE





