class Class1:
    def met(self):
        print("In Class1")
class Class2(Class1):
    def met(self):
        print("In Class2")
class Class3(Class1):
    def met(self):
        print("In Class3")
class Class4(Class3, Class2):
    def met(self):
        print("In Class4")

obj = Class4()
obj.met()

print(Class4.mro())
