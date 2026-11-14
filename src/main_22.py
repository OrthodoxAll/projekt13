class Employee:
    name: str  # Здесь мы пишем название атрибута и указываем тип
    surname: str
    pay: int
    email: str

    def __init__(self,name,surname,pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f'{self.name}.{self.surname}@mail.com'
        self.is_work = False
        self.is_vacation = False

    def work(self):
        self.is_work = True
        self.is_vacation = False
        print('Do siome work')

    def go_to_vacation(self):
        self.is_vacation = True
        self.is_work = False
        print('Do siome go to vacation')

if __name__ == '__main__':
    emp1 = Employee('James','Smith',100)
    print(emp1)
    print(emp1.name)
    print(emp1.surname)
    print(emp1.pay)
    print(emp1.email)
