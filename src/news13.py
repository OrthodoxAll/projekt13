import os
import logging
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_N")
BASE_URL = os.getenv("BASE_URL")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('E:/Digital/bakend_programm/Project13/logs/news.log', encoding= 'utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)




def get_news(query:str,exclude_words:list, api_key = API_KEY) -> list:
    today = datetime.datetime.today()
    params = {
        "q": query,
        #'from': today.strftime("%Y-%m-%d"),
        'sortBy': 'publishedAt',
        'apiKey': api_key
    }
    try:
        logger.info(f'Выполняем запрос с ключевыми словами {query}')
        response = requests.get(
            url=BASE_URL,
            params=params
        )

        news_data = response.json()
        if news_data.get('status') != 'ok':
            logger.info(f'Статей не нашлось')
            return []

        articles_list = news_data.get('articles',[])
        print(articles_list)
        articles_result = []
        for article in articles_list:
            logger.info(f'Фильтруем запрос по словам исключениям {", ".join(exclude_words)}')
            content = f'{article.get('title')} {article.get("content")}'.lower()
            if any(word.lower() in content for word in exclude_words):
                continue
            # exclude_flag = False
            #
            # for word in exclude_words:
            #     if word in content:
            #         exclude_flag = True
            #
            # if exclude_flag:
            #     continue

            articles_result.append({
                'title': article.get('title'),
                'author': article.get('author'),
                'description': article.get('content'),
                'url': article.get('url'),

            })

        return articles_result
    except requests.exceptions.RequestException as ex:
        logger.error(f'Произошла ошибка: {ex}')
        return []
    except Exception as ex:
        logger.error(f'Произошла ошибка 2: {ex}')
        return []