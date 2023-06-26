class Animals:
    def display1(self):
        print("Animals")
class Dog(Animals):
    def display2(self):
        print("Dog")
class Puppy(Dog):
    def display3(self):
        print("Puppy")
        
obj=Puppy()
obj.display1()
obj.display2()
obj.display3()