# Tasks

from sqlmodel import Field, SQLModel, create_engine
from datetime import date

class Task(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    start: str
    end: str

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.description} - {self.status}"
    
    @property
    def duration(self):
        return  self.end - self.start