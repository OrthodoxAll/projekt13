from src.news13 import get_news
from src.safe_to_file import safe_to_file
import datetime

def news():
    '''Функция для работы с приложением'''
    query = "tesla"
    today = datetime.datetime.today()
    today_string = today.strftime('%Y-%m-%d')

    articles_list = get_news(query,['Сириус Автодром 2026','President Trump'] )


    file_name = f'{today_string}_{query.replace(" ","_")}.json'
    file_path = f'news/{file_name}'
    safe_to_file(articles_list,file_path)

   # print(articles_list)








if __name__ == "__main__":
    news()