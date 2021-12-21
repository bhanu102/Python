# creating a class and an instance
class Employee:
    
    no_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.no_of_employees += 1
        
    def fullname(self):
        return f'{self.first} {self.last}'
        
    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
print(Employee.no_of_employees)
emp1 = Employee('Bhanu','Gadupudi',60000)
emp2 = Employee('Murali','Donepudi',70000)
print(Employee.no_of_employees)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.pay)
emp1.pay_raise()
print(emp1.pay)

