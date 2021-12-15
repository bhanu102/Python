class Employee:
    
    no_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'
        
        Employee.no_of_employees += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
        
    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod
    def is_workday(day):
        if day == 5 or day == 6:
            return False
        return True

print(Employee.no_of_employees)
emp1 = Employee('bhanu', 'gadupudi', 70000)
emp2 = Employee('bhanu', 'gadupudi', 70000)
print(Employee.no_of_employees)
print(emp1.pay)
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
emp1.pay_raise()
print(emp1.pay)
emp_str1 = 'bhanu-gadupudi-70000'
new_emp1 = Employee.from_string(emp_str1)
print(new_emp1.email)

import datetime
my_date = datetime.date(2021, 12, 15)
day = my_date.weekday()

print(Employee.is_workday(day))
