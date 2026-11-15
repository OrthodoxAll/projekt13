import datetime
from os import name


class Task:
    name: str
    description: str
    status: str
    created_at: str





    def __init__(self, name, description, status ='Waiting start', created_at= None):
        self.name = name
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.date.today().strftime('%d-%m-%Y')


if __name__ == "__main__":
    task = Task ('Купить огурцы', 'Купить огурцы для салата')
    print(task.name)
    print(task.description)
    print(task.status)
    print(task.created_at)