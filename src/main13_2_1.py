import re
from collections import Counter, defaultdict

text = 'text = "The price of the product is $100.50", R1000.20'

result = re.findall(r'[$R]\d+\.\d', text)

print(result)


text = '''
Visit my website at https://www.example.com
or you can check out https://www.someotherexample.com
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

mathess = pattern.finditer(text)

urls = [match.group(3) for match in mathess]
print(urls)


text = 'Позвоните мне по номеру 555-123-4567 или 555-987-6543'

pattern = re.compile(r'(\d{3}-\d{3}-\d{4})')

phone_numbers  = pattern.findall(text)

print(phone_numbers)


text = 'Цвет неба - синий.'

new_text = re.sub(r'синий', 'blue', text)

print(new_text)


# Создаем строку
my_string = 'abbcccddddeeeee'
# Создаем объект Counter на основе строки
counted = Counter(my_string)
# Выводим результаты подсчета
counted.subtract('abbcccddeeee')
print(counted)



# Создаем defaultdict, который возвращает 0 для отсутствующих ключей
my_dict = defaultdict(int)
# Добавляем значение
my_dict['one'] = 1
# Выводим существующее значение
print(my_dict['one'])
# Выводим значение для отсутствующего ключа
print(my_dict['two'])


# Определяем функцию для значений по умолчанию
def default_value():
    return 2

# Создаем defaultdict с функцией по умолчанию
my_dict = defaultdict(default_value)
# Выводим значение для отсутствующего ключа
print(my_dict['tr4ee'])

