from functools import wraps

def check_floats(precision=0):
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


@check_floats()
def square_1(x):
    '''Возводит в квадрат и добавляет хвост'''
    return (x * x) + 1.23456

print(square_1(3))



from functools import wraps

def shorten_words(max_len, *, end_symbol='.'):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            # words = result.split()
            # shortened_words = []
            # for word in words:
            #     if len(word) > max_len:
            #         shortened_word = word[:max_len] + end_symbol
            #         shortened_words.append(shortened_word)
            #     else:
            #         shortened_words.append(word)
            # return " ".join(shortened_words)
            return " ".join(f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word for word in result.split())
        return inner
    return wrapper



@shorten_words(4, end_symbol='!')
def get_text():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Тесты
def test_shortening():
    assert get_text() == "Lore! ipsu! dolo! sit amet! cons! adip! elit!"

def test_no_shortening():
    @shorten_words(10, end_symbol='!')
    def get_long_text():
        return "Lorem ipsum dolor sit amet"
    assert get_long_text() == "Lorem ipsum dolor sit amet"

def test_end_symbol():
    @shorten_words(3, end_symbol='?')
    def get_questioned_text():
        return "Lorem ipsum dolor"
    assert get_questioned_text() == "Lor? ips? dol?"

def test_different_lengths():
    @shorten_words(5, end_symbol='.')
    def get_different_length_text():
        return "Hello beautiful world"
    assert get_different_length_text() == "Hello beaut. world"