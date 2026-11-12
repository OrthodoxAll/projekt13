import time
import functools

def retry(retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except ConnectionError as e:
                    last_exception = e
                    print(f"Попытка {attempt + 1} не удалась: {e}. Перезапуск через 1 секунду...")
                    time.sleep(1)
            raise last_exception
        return wrapper
    return decorator

# Пример использования декоратора

import random

@retry(retries=5)
def api_call():
    if random.choice([True, False]):
        print("API запрос успешно выполнен")
        return "Успешно"
    else:
        print("API запрос не выполнен")
        raise ConnectionError("Подключение к API не удалось")

# Примеры вызова функции
try:
    result = api_call()
    print(result)
except ConnectionError as e:
    print(f"API запрос не выполнен после переотправки: {e}")
# Тесты:
#
# import pytest
# from unittest.mock import patch, call
#
# # Импортируйте декоратор retry из модуля, где он определен
# from my_module import retry
#
# def test_retry_success():
#     @retry(retries=3)
#     def mock_api_call():
#         return "Успешно"
#
#     with patch('my_module.time.sleep', return_value=None) as mock_sleep:
#         result = mock_api_call()
#         assert result == "Успешно"
#         mock_sleep.assert_not_called()
#
# def test_retry_failure_then_success():
#     call_counts = []
#
#     @retry(retries=3)
#     def mock_api_call():
#         call_counts.append(1)
#         if len(call_counts) < 3:
#             raise ConnectionError("Подключение к API не удалось")
#         return "Успешно"
#
#     with patch('my_module.time.sleep', return_value=None) as mock_sleep:
#         result = mock_api_call()
#         assert result == "Успешно"
#         assert len(call_counts) == 3
#         assert mock_sleep.call_count == 2
#         assert mock_sleep.call_args == call(1)
#
# def test_retry_failure():
#     call_counts = []
#
#     @retry(retries=3)
#     def mock_api_call():
#         call_counts.append(1)
#         raise ConnectionError("Подключение к API не удалось")
#
#     with patch('my_module.time.sleep', return_value=None) as mock_sleep:
#         with pytest.raises(ConnectionError, match="Подключение к API не удалось"):
#             mock_api_call()
#         assert len(call_counts) == 3
#         assert mock_sleep.call_count == 3
#         assert mock_sleep.call_args == call(1)