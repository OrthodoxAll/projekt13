import requests
import json
import logging

logging.basicConfig(
    filename='application.log',
    filemode='a+',
    format='%(levelname)s:%(name)s:Requests time: %(asctime)s',
    level=logging.INFO
)


logger = logging.getLogger()
URL= 'https://jsonplaceholder.typicode.com/users'


def get_users_and_save()->None:
    """получение пользователей и сохранение в файл"""
    response = requests.get(URL)
    logger.info('Done')
    with open('users.json', 'w') as ussers_file:
        json.dump(response.json(), ussers_file)



if __name__ == '__main__':
    get_users_and_save()
