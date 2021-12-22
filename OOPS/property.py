class Person:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        if pay >= 0 :
            self._pay = pay
        else:
            self._pay = 0
            
    @property
    def pay(self):
        return self._pay
        
    @pay.setter
    def pay(self, newpay):
        if newpay >= 0:
            self._pay = newpay
        else:
            return ValueError("Pay cannot be negative.")

p = Person("Bhanu", "Prakash", 70000)
print(p.pay)
p.pay = 80000
print(p.pay)
