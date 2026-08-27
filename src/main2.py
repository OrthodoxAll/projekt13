import random
from itertools import chain

result = (x**3  for x in range(10) if x % 2 == 0)

print(list(result))

my_list = [1, 2, 3]
my_iter = iter(my_list)  # Преобразуем список в итератор

print(next(my_iter))  # Вывод: 1
print(next(my_iter))  # Вывод: 2
print(next(my_iter))  # Вывод: 3



print(''.join(x for x in "Hello World!" if x.isupper()))

def sum_numbers(list_of_numbers):
    result=(x**2 for x in list_of_numbers if x > 0)
    print(sum(result))


vowels = (x for x in 'Hello' if x in ['a', 'e', 'i', 'o', 'u'])
print(list(vowels))


avg_1 = list((x  for x  in range(1,101) if x % 3 == 0 or x % 5 == 0))
result = sum(avg_1)/len(avg_1)
print(result)

numbers = range(1, 101)
filtered_numbers = list(filter(lambda x : x % 5 == 0 or x % 3 == 0, numbers))
average= sum(filtered_numbers)/len(filtered_numbers)
print(average)


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

cobined_list= list(set(chain(list1, list2, list3)))
print(cobined_list)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

filtered_people = list(filter(lambda  x: x['age'] == 30, people))
print(filtered_people)


def inf_seq(start=1):
    while True:
        yield start
        start += 1

numbers = inf_seq()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))

print(next(gen))

print(next(gen))

for value in simple_generator():
    print(value)

def iterate(x0, m):
    x = x0
    while True:
        yield x  # вместо print()
        x *= m

#for n in iterate(1, 1.2):
    # print(n)
    # if n > 3:
    #     break

def f():
    print('Initializing...')
    yield 'one'
    print('Continue...')
    yield 'two'
    print('Stopping...')

i = f()
print(next(i))
print(next(i))

if __name__ == '__main__':
    # test
    i = iterate(1, 1.2)
    assert next(i) == 1
    assert next(i) == 1.2
    assert next(i) == 1.44
    assert next(i) == 1.728


def square_generator(nums):
    for num in nums:
        yield num ** 2


def random_number_generator(start, stop):
    while True:
        yield random.randint(start, stop)

print(next(random_number_generator(5,7)))
print(next(random_number_generator(5,7)))
print(next(random_number_generator(5,7)))
print(next(random_number_generator(5,7)))


def intersection_generator(lst1, lst2):
    seen = set()
    for item in lst1:
        if item in lst2 and item not in seen:
            seen.add(item)
            yield item




def spiral_generator(n):
    matrix = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2
    dx, dy = 0, -1
    num = 1

    for _ in range(n * n):
        if -n // 2 < x <= n // 2 and -n // 2 < y <= n // 2:
            matrix[y][x] = num
            yield num
            num += 1

        if x == y or (x < y and x + y < n - 1) or (x > y and x + y >= n):
            dx, dy = -dy, dx

        x, y = x + dx, y + dy

numbers = list(spiral_generator(20))  # Преобразуем генератор в список
print(numbers)