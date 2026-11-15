import pytest

from src.oop_additional_tasks.lesson1.user import User
from src.oop_additional_tasks.lesson1.task import Task

@pytest.fixture
def data():
    return {
        'first_names': ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah'],
        'last_names': ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson'],
        'cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    }
@pytest.fixture

def first_user():
    return User(
        username='User',
        email='user@localhost',
        first_name='John',
        last_name='Smith',
        task_list= [
            Task('Купить огурцы', 'Купить огурцы для салата'),
            Task('Купить морковь', 'Купить морковь для салата'),
        ]
    )

@pytest.fixture
def second_user():
    return User(
        username='Piter',
        email='Peter@localhost',
        first_name='Piter',
        last_name='Piterson',
        task_list= [
            Task('Купить лук', 'Купить лук для салата'),
            Task('Купить помедоры', 'Купить помедоры для салата'),
            Task('Купить масло', 'Купить маслдор для салата')
        ]
    )

@pytest.fixture

def task():
    return Task('Купить огурцы', 'Купить огурцы для салата', created_at="12.10.2024")