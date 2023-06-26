class Deepak:  
    def __init__(self,name,id,age):  
        self.name = name  
        self.id = id  
        self.age = age  

d = Deepak("Deep", 45, 19)  

print(getattr(d, 'name'))  
setattr(d, "age", 19)  
print(getattr(d, 'age'))  
print(hasattr(d, 'id'))  
delattr(d, 'age')  
#print(s.age)  