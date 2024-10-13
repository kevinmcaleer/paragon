from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel

app = FastAPI()

projects = {
    "1": {
        "name": "Project 1",
        "description": "A simple project",
        "tasks": []
    }
}

sqlite_file_name = "paragon.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/projects")
# def read_projects():
#     return {"data": "projects"}
