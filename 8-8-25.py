1. Write a function that takes two numbers and prints their sum.

def sum(a,b,op):
    if op=="+" or op=="add":
        print(a+b)
    else:
        print("invalid operator")
sum(2,4,"*")        

2.Write a function that prints the square of a number.

def square(a):
    if a>0:
        print(a**2)
square(10)        

3.Write a function to check if a number is even or odd and print the result.

def even_or_odd(n):
    print("even") if n%2==0 else print("odd")
# even_or_odd(6)

4.Write a function that prints the factorial of a number.

def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*n
        n-=1
    print(sum)
factorial(6)        

5.Write a function to find the maximum of three numbers and print it.

def max(a,b,c):
    print(a) if a>b or a>c else print(b) if b>c else print(c)
max(5,6,7)

6.Write a function to count and print the number of vowels in a string.
def vowels(n):
    vowels="aeiouAEIOU"
    count=0
    sum=1
    for i in n:
        if i in vowels:
            count=count+sum
            print(count)
p=str(input("enter the number:"))  
vowels(p)


7.Write a function that takes a list and prints the sum of all elements.
def sum_of_elements(n):
    total=sum(n)
    print(total)
n=[1,2,3,4]
sum_of_elements(n)    
        
8.Write a function to reverse a string and print it.
def reverse(n):
    print(n[::-1])
n=str(input("enter the num:"))  
reverse(n)  

9.Write a function that checks if a string is a palindrome and prints the result
def palindrome(n):
    if n==n[::-1]:
        print("palindrome")
    else:
        print("not a polindrome")
n=str(input("enter the string:"))      
palindrome(n)  



10.Write a function that takes a list and prints only the even numbers.

def even(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
even(5)  

11.Write a function to calculate and print the area of a circle given its radius.
def radius(r):
    pie=3.14
    print(pie*r**2)
radius(4)  

12.Write a function that prints the length of a string without using the len() function.  

def length(n):
    print(len(n))
n=input("enter the numbers:")    
length(n)

13.Write a function that accepts any number of arguments and prints their average.
def average(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+n
        n-=1
    print(sum/i)    
average(28)              

