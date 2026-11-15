from src.oop_additional_tasks.lesson1.task import Task

class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count =0
    all_tasks_count  = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = task_list if task_list is not None else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list is not None else []


if __name__ == '__main__':
    task1 = Task ('Купить огурцы', 'Купить огурцы для салата')
    task2 = Task('Купить морковь', 'Купить морковь для салата')
    task3 = Task('Купить лук', 'Купить лук для салата')
    task4= Task('Купить помедоры', 'Купить помедоры для салата')

    user = User('User', 'user@mail', 'User', 'Userov' , [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(user.all_tasks_count)
