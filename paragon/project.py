# Projects 

from pydantic import BaseModel, Field

from .task import Task

class Project(BaseModel):

    name: str = Field(examples=['Project 1', 'Project 2'])
    description: str = Field(examples=['A simple project', 'A complex project'])
    _tasks: [Task] = Field

    def __init__(self, name, description, tasks):
        self.name = name
        self.description = description
        self._tasks = tasks

    def __str__(self):
        return f'Project: {self.name}'
    
    @property
    def tasks(self):
        return self._tasks
    
    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks