# Question 1:  Create your own class which can implement all arthematic operations.
#              Create 2 objects for it and call above implemented methods. Add model_num, made_in variables to obj1. 
#             Add color and discount to obj2. print model_num, made_in, color, discount to both the object

# Create your own class which can implement all arthematic operations.
class arithmatic():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        if b!=0:
            print(a/b)
        else:
            print("not divisible")  
    def floor(self,a,b):
        print(a//b) 
    def power(self,a,b):
        print(a**b)  
    def mod(self,a,b):
        print(a%b)    
    def discribe(self):
        print(self.model_num,self.made_in,self.color,self.discount)  

# Create 2 objects for it and call above implemented methods        
a1=arithmatic()  
a2=arithmatic() 

a1.add(1,2)   
a1.sub(2,4) 
a1.mul(2,6)
a1.div(2,0)   
a2.floor(2,5)
a2.power(2,8)
a2.mod(9,5)

#object1
a1.model_num="basheer"
a1.made_in="andhra"
a1.color="black"
a1.discount="20%"
print(a1.model_num)
print(a1.made_in)
print(a1.color)
print(a1.discount)

# object2

a2.color="pink"
a2.discount="50%"
a2.model_num="abdulla"
a2.made_in="nandyal"
print(a2.color)
print(a2.discount)
print(a2.model_num)
print(a2.made_in)

a1.discribe()
a2.discribe()

#2. Define self---
self is a reference to the instance of the class. it is used to access instance variables 
and methods within the class
        