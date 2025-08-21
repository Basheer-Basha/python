# # method 1
# # n=int(input("enter the number:"))
# # count=0
# # for i in range (1,n+1):
# #     if n%i==0:
# #         count+=1
# # if count==2:
# #     print("prime number")   
# # else:
# #     print("not a prime number")    
    
# #method 2
# # num1=int(input("enter the number:"))
# # if num1<=1:
# #     print("not a prime")
# # else:
# #     flag=True
# #     for i in range(2,num1):
# #         if num1%i==0:
# #             flag=False
# #             print("not a prime")
# #             break
# #     if flag==True:
# #         print("prime")  
        
# #method 3
# # def prime(n):
# #     if n<=1:
# #         return("not a prime")        
# #     for i in range(2,n):
# #         if n%i==0:
# #             return "not a prime" 
# #     return "prime"    
# # n=int(input("enter the number:"))
# # r=prime(n)
# # print(r)

# # def prime(n):
# #     if n<=1:
# #         return("not a prime")        
# #     for i in range(2,n//2+1):
# #         if n%i==0:
# #             return "not a prime"
# #     return "prime"    
# # n=int(input("enter the number:"))
# # r=prime(n)
# # print(r)
# # n=int(input("enter the number:"))
# # for i in range(1,n+1):
# #     if n%i==0:
# #         print(i)

# # def prime(n):
# #     if n<=1:
# #         return("not a prime")
# #     else:
# #         for i in range(2,int(n**0.5)+1):
# #             if n%i==0:
# #                 return("not a prime")
# #                 break
# #         return("prime")  
# # n=int(input("enter the string:"))   
# # s=print(n)  
# # print(s)    

# # while True:
# #     number=["square","cube"]
# #     print(number)
# #     n=input("choose the option:")
# #     if n in number:
# #         a=int(input("enter the number:"))
# #         if n=="square":
# #             print(a**2)
# #         elif n=="cube":
# #             print(a**3)
            
            
# #     else:
# #         print("Exit")
# #         break

# # ip1=int(input("enter the number 1:"))
# # ip2=int(input("enter the number 2:"))
# # for i in range(ip1,ip2+1):
# #     res==check_prime(i)
# #     if res:
# #         print(i)
# #     if check_prime(i):
# #         print(i)

# #Fibnocci numbers => print first n fib numbers
# #like=> 0 1 1 2 3 5 8 13 etc...
# #sum of previous number is new number.

# # n=10
# # num1,num2=0,1
# # for i in range(0,n):
# #     print(num1)
# #     new_num=num1+num2
# #     num1=num2
# #     num2=new_num

# #armstrong number=> sum of 3 or 4 digits of cube is equal to that digits

# # n=153
# # n1=n
# # s=0
# # while n>0:
# #     rem=n % 10
# #     s+=rem**len(str(n1))
# #     n=n//10
# # print(s)
# # if s==n1:
# #     print("armstrong")    
# # else:
# #     print("not")

# # n=6
# # count=0
# # sum=0
# # for i in range(1,n+1):
# #     if n%i==0:
# #         count+=1
# #         sum=i
# #         print(sum)
        
# # if count==2:
# #     print("prime")   
# # else:
# #     print("not")   

# # n=153
# # sum=0
# # temp=n
# # for i in str(n):
# #     rem=temp%10
# #     sum=rem**3
# # print(sum)
# # n=10
# # count=0
# # for i in range(1,n+1):
# #     if n%i!=0:
# #         print(i)
# # if count==2:
# #     print("prime")
# # else:
# #     print("not prime")

# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     for i in range(2, n):
# #         if n % i == 0:
# #             return False
# #     return True

# # start = 1
# # end = 50
# # primes = []
# # for n in range(start, end + 1):
# #     if is_prime(n):
# #         primes=n
# #         print(primes)   


# n=int(input("enter the number:"))
# # count=0
# # for i in range (1,n+1):
# #     if n%i==0:
# #         count+=1
# # if count==2:
# #     print("prime number")   
# # else:
# #     print("not a prime number") 
    
# start=1
# count=0
# prime=[]
# if n<=1:
#     print("not a prime")
# for i in range(start,n+1) :
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")   
# else:
#     print("not a prime")
         
           
for i in range(1,6):
    for j in range(1,11):
        print(i,"X",j,"=",i*j)           
        
# for i in range(5):
#     for i in range(6):
#         print(i*j)        
            
# l=[[1,2,3],[3,4,5],[4,7,8]] 
# count=0 
# for i in l:
#     count=i
#     a=sum(count)
#     print(a)
    
# # l1=print(sum(l[0]),sum(l[1]),sum(l[2]) )  
# l=[[1,2,3],[3,4,5],[4,7,8]] 
# for i in l:
#     count=0
#     for j in i:
#         count+=j 
#     print(count)
    
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()     
    
n=4
for i in range(n,0,-1)    :
    for j in range(i,0,-1):
        print(j,end=" ")
    print()    
    
   
    

    
    
    
    
      
        
        


 