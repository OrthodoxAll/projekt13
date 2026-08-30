from time import time

from functools import wraps


def create_counter():
    count = [0]

    def counter():
        count[0] += 1
        return count[0]

    return counter


my_counter = create_counter()

print(my_counter()) # 1
print(my_counter()) # 2
print(my_counter()) # 3
print(my_counter()) # 4

def timer(func):

    def wrapper(*args, **kwargs):
        timee_1 = time()
        result = func(*args, **kwargs)
        timee_2 = time()
        print(f'Time for work: {timee_2 - timee_1}')
        return result
    return wrapper

@timer
def example():
    for i in range(1000000000):
        continue

example()


def inter(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if type (x)==float else x for x in result]
            return type(result)(rounded)
        else:
            return result
    return wrapper

@inter
def calculate():
    return 3.6

@inter
def calculate_list():
    return [3.6, 1.1, 5, 2.2]

print(calculate())
print(calculate_list())

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(2):
            try:
                return func(*args, **kwargs)
            except :
                time.sleep(3)
            raise Exception('Function call failed after multiple retries')
    return wrapper

@retry
def unreliable_function():
    import random
    # Эмулируем случайные ошибки
    if random.choice([False, False]):
        raise ValueError('Error occurred!')
    return 'Success!'
print(unreliable_function())  # Попробует выполнить функцию до 3 раз


def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("!", "!!!")
    return wrapper

def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace("?", "???")
    return wrapper

def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(".", "...")
    return wrapper

@exclamation_marks
@question_marks
@dots
def my_function():
    return "This is a sentence. It has a question? Does it need more exclamation!"

print(my_function())

def checking_that_arg_is(predicate, error_message):
    def wrapper(function):
        @wraps(function)
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)
        return inner
    return wrapper

def predicate(x):
    return type(x) == int

def predicate_is_positive(x):
    return x>0

@checking_that_arg_is(predicate_is_positive, "Значение должно быть положительным")
@checking_that_arg_is(predicate, "Значение должно быть целым числом")
def square(x):
    '''Возводит в квадрат'''
    return x * x

print(help(square))

print(square(4))

def check_floats(precision):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            # Проверка на тип с использованием type()
            if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in result]
                return type(result)(rounded)
            else:
                return result
        return inner
    return decorator


@check_floats(3)
def square_1(x):
    '''Возводит в квадрат и добавляет хвост'''
    return (x * x) + 1.23456

print(square_1(3))

print(help(square_1))

