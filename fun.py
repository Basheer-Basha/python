# Functions:
# It is a block of code,which gets executed whenever you call it.
# function keyword is "def".arguments is to assign the values in calling the function. this argument value can be written in parameter"()"".
# Keyword arguments->it is using to assign the value by using parameter key.like a=1,b=2 etc./

# n={1:"basheer",
#    2:"srinu"}
# def basheer():
#     print(n)
#     print((4/3)*3.14*(10**3))

# # print("another")     
# basheer()
# basheer()
# print(type(n))

# def basheer(r):
#     print("calculate volume of sphere")
#     print((4/3)*3.14*(r**3))
#     print("calculated volume")
# basheer(3)
# basheer(7)   
# basheer(10) 

# def simple_calc(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b) 
#     if b!=0:
#         print(a%b)
#         print(a/b)
#         print(a//b)
#     else:
#         print("not divisible")
# simple_calc(2,0)    
# simple_calc(3,4)

# def table_calc(n):
#     for i in range(1,21):
#         print(n,"X",i,"=",n*i)
        
# table_calc(12)
# table_calc(20)
# table_calc(2)
# table_calc(7)
                
# def sum_cal(n):
#     sum=0
#     for i in range(1,n+1):  
#       sum=sum+i 
#     print(sum)
# sum_cal(10)

# def greater(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)
# greater(b=6,a=4,c=5)        

# positional operator->the values is given to if function is calling.
#Keyword arguments->it is using to assign the value by using parameter key.like a=1,b=2 etc./
#default ardument->the values are given in function itself.

# def lap(b,a=4):
#     count=0    
#     for i in range(1,7):
#         for i in range(5):
#             count=a+b
#     print(count)        
# lap(1)  
# lap(4,a=1)
# lap(b=5)     

# arbitrary arguments
# def pre(a,c,*b):
#     print(a)
#     print(sum(b))
#     print(c)
# pre(2,33,44)
# pre(22,2,532)

#Key words arbitrary arguments;
#keyword of arguments is represented as-> (**args)
# def basheer(**args):
#     print(args)
#     print(type(args))
# basheer(bas="bash",pas=223,bash="jhewhdg",password=6235,args=123)

# return statement
# def add(num1,num2):
#     print(num1+num2)
#     return num1+num2
# add(2,3)
# result=add(4,7)  
# print(result*8)  

# def basheer(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
    
# r=basheer(3)
# print(r)
# print(str(r)) 
# # print(type(r)) 
# r1=basheer(76)
# print(r1)
# print(type(r1))

# #single return statement ->we can write  multiple values can be write

# def bas(a,b):
#     return a+b,a-b,a*b 
# r1=bas(10,12)
# print(r1)
# print(type(r1))

# # return statement is once executed can be consider as end of the function.

# def bas(n):
#     for i in range(1,n):
#         print(i)
#         if i==7:
#             return
#     return 45
# print(bas(22))    

    
    
    
