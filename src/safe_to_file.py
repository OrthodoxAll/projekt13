import os
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('E:/Digital/bakend_programm/Project13/logs/safe_to_file.log', encoding= 'utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def safe_to_file(data: list, file_path: str) -> None:
    """
    safe to file in pфth
    :param data:
    :param path:
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        logger.info(f"Записываем данные в фаил {file_path}")
        with open(file_path, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file)
    except Exception as e:
        logger.error(f"Ошибка при сохранении файла: {e}")
      
