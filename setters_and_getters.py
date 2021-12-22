class Person:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        if pay >= 0:
            self._pay = pay
        else:
            self._pay = 0
    def getPay(self):
        return self._pay
        
    def setPay(self, newpay):
        if newpay > 0:
            self._pay = newpay
        else:
            return ValueError("Pay cannot be negative")
p = Person("Bhanu", "Gadupudi", 70000)
print(p.getPay())
p.setPay(80000)
print(p.getPay())
