import datetime



def get_days_between_dates(date1:str, date2:str) -> int:
    '''принимает на вход имя пользователя GitHub и
     возвращает список названий репозиториев этого пользователя.'''
    date1_obj = datetime.datetime.strptime(date1, '%d.%m.%Y')
    date2_obj = datetime.datetime.strptime(date2, '%d.%m.%Y')
    delta = date2_obj - date1_obj
    print(delta.days)


get_days_between_dates("01.01.2022", "31.01.2022")
 ######