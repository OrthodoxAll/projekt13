import requests


def get_github_repos(username: str) -> list[str]:
    '''
    возвращает список названий репозиториев
    :param username: 
    :return: 
    '''
    url=f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repos = [repo['full_name'] for repo in response.json()]
    else:
        repos = []
    return repos


repos=get_github_repos('octocahjgvhjkfghjkt')
print(repos)

