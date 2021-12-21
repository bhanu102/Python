class person_details:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
class birth_details(person_details):
    def __init__(self, first, last, pay, age, place_of_birth, country = "India" ):
        super().__init__(first, last, pay)
        self.age = age
        self.place_of_birth = place_of_birth
        self.country = country
        
person1 = birth_details("Bhanu", "Gadupudi", 70000, 21, "Chandarlapadu")

person2 = birth_details("Joe", "Smith", 80000, 22, "Nandigama")

print(person1.place_of_birth)
print(person1.first)
print(person1.age)
print(person2.country)
