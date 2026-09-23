from src.news13 import get_news
from src.safe_to_file import safe_to_file
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('E:/Digital/bakend_programm/Project13/logs/news13_1.log', encoding= 'utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



def news():
    '''Функция для работы с приложением'''
    try:
        query = input('Ввыедите ключевые слова: ')
        exclude_words = input('Введите слова для фильтрации, через ",": ').split(',')
        today = datetime.datetime.today()
        today_string = today.strftime('%Y-%m-%d')
        logger.info('Получение новостей')

        articles_list = get_news(query,exclude_words )

        logger.info('Запись новостей в файл')

        file_name = f'{today_string}_{query.replace(" ","_")}.json'
        file_path = f'E:/Digital/bakend_programm/Project13/news/{file_name}'
        safe_to_file(articles_list,file_path)
    except Exception as e:
        logger.error(f"Ошибка : {e}")
   # print(articles_list)








if __name__ == "__main__":
    news()