import pytest

@pytest.fixture
def data():
    return {
        'first_names': ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah'],
        'last_names': ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson'],
        'cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    }