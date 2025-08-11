# # def number(a=8):
# #     if a<0:
# #         print("negative")
# #     elif a>0:
# #         print("positive")
# #     else:
# #         print("zero")
# # number()        
# # number(4)        
# # number(-5)
# # number(0)

# # def num(a):
# #     if a%2==0:
# #         print("even")
# #     else:
# #         print("odd")
        
# # num(5)
# # num(10)    

# #terminary operator->
# # num=float(input("enter the num:"))
# # print("even") if num%2==0 else print("odd")

# # def even_or_odd(num1):
# #     return "even" if num1%2==0 else "odd"
# # even_or_odd(3)


# def vote(a):
#     print ("eligible") if a>=18 else print("not eligible")
        
# vote(18)        

# def vote1(b):
#     if b>=18:
#         return"eligible"
#     else:
#         return "not eligible"
# a=vote1(12)    
# c=vote1(18)
# print(a)
# print(c)

# def greater(num1,num2):
#     if num1>num2:
#         return(num1)
#     elif num1==num2:
#         return("both are same")
#     else:
#         return(num2)
# a=greater(2,4)
# b=greater(2,2)
# c=greater(4,3)
# print(a)
# print(b)
# print(c)
# # terminatory operator:
# def basheer(a,b):
#     print(a) if a>b else print("both are equal") if a==b else print(b)
# basheer(2,4)
# basheer(3,7)
# basheer(7,7)

# def calc(a,b,op):
#     if op in ["+","add"]:
#         print(a+b)
#     elif op=="-":
#         print(a-b)
#     elif op=="*":
#         print(a*b)
#     elif op=="%":
#         print(a%b) if b!=0 else print("division not avalable")
#     else:
#         print("invalid operator")
# calc(2,4,op="*")
# calc(4,6,op="+")
# calc(2,0,op="%")
# calc(2,4,op="/")
# op=input("enter the operator:").lower()
# calc(2,8,op)
        
# def year(i) :      
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         print("leap year")    
#     else:
#         print("not leap year")
# i=int(input("enter the year:") )       
# year(i)           
# terinary operator->
# def leap_year(i):
#     return("leap year") if (i%4==0 and i%100!=0) or (i%400==0) else "not a leap year"      
# i=int(input("enter the year:"))        
# print(leap_year(i)) 

# def grade(i):
#     if i<70:
#         print("Fail")
#     elif i>=70 or i<=79:
#         print("Grade C")
#     elif i>=80 or i<=89:
#         print("Grade B")
#     else:
#         print("Grade A")
# i=int(input("enter the mark:") )       
# grade(i)        


# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i)
# n=int(input("enter the number:"))        
# even(n)    
# i=2
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=2

# while True:
#     n=int(input("enter the number"))
#     if n>0:
#         print(n)
#     else:
#         print("loop break")
#         break

# while True:
#     op=input("enter the opetrator:")
#     if op in ["+","-","*","%"]:
#         a=int(input("enter the number a:"))
#         b=int(input("enter the number b:"))
#         if op=="+":
#             print(a+b)
#         elif op=="-":
#             print(a-b)
#         elif op=="*":
#             print(a*b)
#         elif op=="%":
#             if b!=0:
#                 print(a%b)# 
#             else:
#                 print("division not possible")
#     else:
#         print("input operator is wrong")
#         break


# def triangle(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         if a==b==c:
#             print("equilant")
#         elif a==b or b==c or a==c:
#             print("isolated ")
#         else:
#             print("scalar")
# s=triangle(1,2,3)
# triangle(s)

n=input("enter the name:")
    
    
    
       
    
   


     