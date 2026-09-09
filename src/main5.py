import json

import random
# book_info= {
#     'title': 'Sherlock Holms',
#     'author': 'Arthur Conno Doyle',
#     'publisher_year': '1887',
#     'genre': ['detective', 'novel']
# }
#
# with open('book_info.json', 'w') as json_file:
#     json.dump(book_info, json_file)
# #
# book_info_str= json.dumps(book_info)
# print (book_info_str)


# book_info_str = '{"title": "Sherlock Holms", "author": "Arthur Conno Doyle", "publisher_year": "1887", "genre": ["detective", "novel"]}'
#
# book_info=json.loads(book_info_str)

# with open('book_info.json') as json_file:
#     book_info = json.load(json_file)
#     print(book_info)
#     print(type(book_info))
#
#
# print(book_info)
# print(type(book_info))



cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']


def generate_users(first_names: list[str], last_names:list[str], cities: list[str]) -> dict:
    '''Utyhbhetn gjkmpjdfntktq'''
    while True:
        user = {
                'first_name' :  random.choice(first_names),
                'last_name'  : random.choice(last_names),
                'cities': random.choice(cities),
                'age' : random.randint(18, 65)
        }
        yield user
# if __name__ == '__main__':
users = generate_users(first_names, last_names, cities)
#
user_group1 = [next(users) for i in range(4)]
user_group2 = [next(users) for i in range(6)]

print('User group #1')
print(json.dumps(user_group1, indent=4))
print('User group #2')
print(json.dumps(user_group2, indent=4))
print('single user')
print(json.dumps(next(users), indent=1 4))



