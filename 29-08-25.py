#find even digits in a number
n=int(input("enter the number:"))
while n>1:
    digits=n%10
    if digits%2==0:
        print(digits)
    n=n//10    
    
    
# Find prime digits in a number.    
n=int(input("enter the number:"))
while n>1:
    digits=n%10
    count=0
    for i in range (1,digits+1):
        if digits%i==0:
            count+=1
    if count==2:
        print(i)              
    n=n//10    
    
# Product of all elements in a matrix   
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
product = 1
for row in matrix:
    for element in row:
        product =product* element
print(product)