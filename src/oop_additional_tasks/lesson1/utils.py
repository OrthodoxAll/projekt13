import json
import os

from src.oop_additional_tasks.lesson1.task import Task
from src.oop_additional_tasks.lesson1.user import User

def read_json(path:str)->dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data= json.load(file)
        return data

def creat_object_from_json(data):
    users =[]
    for user in data:
        tasks =[]
        for task in user['task_list']:
            tasks.append(Task(**task))
        user['task_list'] = tasks
        users.append(User(**user))

    return users

if __name__ == '__main__':
    raw_data = read_json('E:/Digital/bakend_programm/Project13/data/data.json')
    users_data = creat_object_from_json(raw_data)
    print(users_data[0].username)
    print(users_data[1].username)
    print(users_data[1].task_list[0].description)





