class Bird:
    def fly(self):
        print("bird flying")
class Crow(Bird):
    def cawing(self):
        print("crow cawing")
        
ob= Crow()
ob.fly()
ob.cawing()