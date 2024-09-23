# Projects 

from .task import Task

class Project:

    name = ''
    description = ''
    _tasks = [Task]

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