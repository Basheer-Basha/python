# 1.WAP take a list add the that number?
name=[1,2,3,4]
total=0
for i in name:
    total += i
print("sum:",total)
    
# 2.WAP take a list find even number.    
list1=[1,2,3,4,5,6,7,8,9]
for i in list1:
    if i%2==0:
        print(i)
    
    
# 3.WAP PRINT COUNT THE EVEN ODD NUMBERS 1 TO 10? 
even_count = 0
odd_count = 0

for i in range(1, 11):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# 4.SUM OF DIGITS OF A NUMBER EXAMPLE 12322 OUTPUT=10
num =12322
sum_of_digits = 0

for i in str(num):
    sum_of_digits += int(i)

print(sum_of_digits)  


# 5.PRODUCT OF DIGITS OF A NUMBER EXAMPLE 123 OUTPUT=6?

num = 123
product_of_digits = 1

for digit in str(num):
    product_of_digits += int(digit)

print(product_of_digits)   

    
        
        
