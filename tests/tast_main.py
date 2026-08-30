from Project13\src\main.pyimport divider

def test_devider():
    assert divider(2,1) == 6

    assert divider(2,0) == 0



list_x=[x for num in range(20) for x in [num, num] if num % 2 == 0]
print(list_x)





i= (x*x for x in range (10))