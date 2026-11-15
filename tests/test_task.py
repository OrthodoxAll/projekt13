
def test_task_init(task):
    assert task.name == 'Купить огурцы'
    assert task.description == 'Купить огурцы для салата'
    assert task.status == 'Waiting start'
    assert task.created_at == "12.10.2024"
