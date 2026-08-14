def add_numbers(num1, num2):
    return num1 + num2



def is_even(num):
    return num % 2 == 0



def find_max(my_list):
    if len(my_list) > 0:
         return max(my_list)
    return 0



if __name__ == '__main__':
    assert add_numbers(1, 2) == 3

    assert is_even(0) == True

    assert find_max([]) == 5
