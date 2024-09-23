from paragon.project import Project
from paragon.task import Task

p = Project('Paragon', 'A simple project management tool', [])

t = Task('Task 1', 'A simple task', 'In Progress')

p.tasks.append(t)

print(p.tasks)