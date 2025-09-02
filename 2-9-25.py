#constructor
# A constructor is a special method that is automatically called when an object of a class is created. It is defined using the __init__ method.

class constructor:
    company_name="TVS"
    def __init__(self,id1,name1,age1):
        self.id=id1
        self.name=name1
        self.age=age1
        print("basheer")
        
    def add(self,a,b):
        print(a+b)    
        
    def discribe(self):
        print(self.id,self.name,self.age)    
        
clc1=constructor(1,"basha",22)
clc2=constructor(2,"srinu",22)    
clc1.add(1,3)   
clc1.discribe() 
clc2.discribe()

#variables
#types of variable
#1.instance variable  2.static/class variable
#instance variavle=> Those variables are dependent on an instance
#static/class variable=> Those variables value is not dependent on an instance.
#    It's value is common to all the objects of that class
class constructor:
    company_name="TVS"
    def __init__(self,id1,name1,age1):
        self.id=id1
        self.name=name1
        self.age=age1
        print("basheer")
        
clc1=constructor(1,"basha",22)
clc2=constructor(2,"srinu",22)   
#instance variable
print(clc1.id) 
print(constructor.id)  #it is shows the error
#static/class variable
print(clc1.company_name)
print(constructor.company_name)

#methods
#it has divided into three types they are
#1.instance method 2.class method 3.static method
class constructor:
    company_name="TVS"
    def __init__(self,id1,name1,age1):
        self.id=id1
        self.name=name1
        self.age=age1
        print("basheer")
        
    def add(self,a,b):
        print(a+b)
        print(self.id) 
        
    @classmethod
    def change_company_name(cls,new_name):
        cls.company_name=new_name  
        
    @staticmethod
    def identity(name,age):
        num1=10
        print("basheer basha")      
        
    def discribe(self):
        print(self.id,self.name,self.age)       
        
clc1=constructor(1,"basha",22)
clc2=constructor(2,"srinu",22)   
clc1.add(2,4)
clc2.add(2,6)
clc1.discribe()

clc3=constructor(3,"abdulla",22)
#instance method
clc3.discribe()
constructor.discribe() # it is shows the error to overcome this situation we can write
constructor.discribe(clc3)
#class method
clc3.change_company_name("PULSAR")
constructor.change_company_name("PULSAR")
print(clc3.company_name)
print(constructor.company_name)

#static method
clc3.identity(1,2)
constructor.identity(3,5)






