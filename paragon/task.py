# Tasks

from datetime import date

class Task:

    start = date
    end = date

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.description} - {self.status}"
    
    @property
    def duration(self):
        return  self.end - self.start