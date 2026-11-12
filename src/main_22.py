class Employee:
    name: str  # Здесь мы пишем название атрибута и указываем тип
    surname: str
    pay: int
    email: str

    def __init__(self,name,surname,pay,email):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = f'{self.name}.{self.surname}@mail.com'

    def fullname(self):
        """Метод, который возвращает полное имя сотрудника."""
        return f'{self.name} {self.surname}'  # self позволяет использовать данные конкретного экземпляра

emp_1 = Employee('John','Smith',5000,'')
print(emp_1.name)
print(emp_1.surname)
print(emp_1.pay)
print(emp_1.email)
print(emp_1.fullname())