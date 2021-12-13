# creating a class and an instance
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return f'{self.first} {self.last}'
        
emp1 = Employee('Bhanu','Gadupudi',60000)
print(emp1.first)
print(emp1.fullname())
print(Employee.fullname(emp1))