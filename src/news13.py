import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_N")
BASE_URL = os.getenv("BASE_URL")






def get_news(query:str,exclude_words:list, api_key = API_KEY) -> list:
    today = datetime.datetime.today()
    params = {
        "q": query,
        #'from': today.strftime("%Y-%m-%d"),
        'sortBy': 'publishedAt',
        'apiKey': api_key
    }
    try:

        response = requests.get(
            url=BASE_URL,
            params=params
        )

        news_data = response.json()
        if news_data.get('status') != 'ok':
            return []

        articles_list = news_data.get('articles',[])
        print(articles_list)
        articles_result = []
        for article in articles_list:

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
    except requests.exceptions.RequestException as e:
        return []
    except Exception:
        return []