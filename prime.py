# method 1
# n=int(input("enter the number:"))
# count=0
# for i in range (1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime number")   
# else:
#     print("not a prime number")    
    
#method 2
# num1=int(input("enter the number:"))
# if num1<=1:
#     print("not a prime")
# else:
#     flag=True
#     for i in range(2,num1):
#         if num1%i==0:
#             flag=False
#             print("not a prime")
#             break
#     if flag==True:
#         print("prime")  
        
#method 3
# def prime(n):
#     if n<=1:
#         return("not a prime")        
#     for i in range(2,n):
#         if n%i==0:
#             return "not a prime" 
#     return "prime"    
# n=int(input("enter the number:"))
# r=prime(n)
# print(r)

# def prime(n):
#     if n<=1:
#         return("not a prime")        
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return "not a prime"
#     return "prime"    
# n=int(input("enter the number:"))
# r=prime(n)
# print(r)
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# def prime(n):
#     if n<=1:
#         return("not a prime")
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 return("not a prime")
#                 break
#         return("prime")  
# n=int(input("enter the string:"))   
# s=print(n)  
# print(s)    

while True:
    number=["square","cube"]
    print(number)
    n=input("choose the option:")
    if n in number:
        a=int(input("enter the number:"))
        if n=="square":
            print(a**2)
        elif n=="cube":
            print(a**3)
            
            
    else:
        print("Exit")
        break
   
        
        
        
        


 