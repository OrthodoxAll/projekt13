import os
import json

def safe_to_file(data: list, file_path: str) -> None:
    """
    safe to file in pфth
    :param data:
    :param path:
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
