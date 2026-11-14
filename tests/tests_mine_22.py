import pytest

from src.main_22 import Employee

@pytest.fixture()
def employes_ivan():
    return Employee('Ivan', 'Patrick', 5000)

def test_init(employes_ivan):
    assert employes_ivan.name == 'Ivan'
    assert employes_ivan.surname == 'Patrick'
    assert employes_ivan.email == 'Ivan.Patrick@mail.com'

def test_is_work(employes_ivan):
    assert not employes_ivan.is_work
    employes_ivan.work ()
    assert employes_ivan.is_work

def test_is_work_not_vocation(employes_ivan):
    employes_ivan.go_to_vacation()
    employes_ivan.work()
    assert not employes_ivan.is_vacation

def test_is_vocation(employes_ivan):
    assert not employes_ivan.is_vacation
    employes_ivan.go_to_vacation()
    assert employes_ivan.is_vacation


def test_is_vacation_not_work(employes_ivan):
    employes_ivan.work()
    employes_ivan.go_to_vacation()
    assert not employes_ivan.work()
