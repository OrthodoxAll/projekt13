from src.news13 import get_news
from src.safe_to_file import safe_to_file
import datetime

def news():
    '''Функция для работы с приложением'''
    query = input('Ввыедите ключевые слова: ')
    exclude_words = input('Введите слова для фильтрации, через ",": ').split(',')
    today = datetime.datetime.today()
    today_string = today.strftime('%Y-%m-%d')

    articles_list = get_news(query,exclude_words )


    file_name = f'{today_string}_{query.replace(" ","_")}.json'
    file_path = f'E:/Digital/bakend_programm/Project13/news/{file_name}'
    safe_to_file(articles_list,file_path)

   # print(articles_list)








if __name__ == "__main__":
    news()