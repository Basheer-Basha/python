# Palindromic Bus Ticket
n=str(input("enter the bus ticket:"))
if n==n[::-1]:
    print("Lucky Ticket")
else:
    print("Not Lucky")

# enter the bus ticket: 123
# Not Lucky
# enter the bus ticket:121
# Lucky Ticket    

# Sum of Magic Squares

n=int(input("enter the number:"))
basheer=0
for i in range(1,n+1):
    basheer=basheer+i**2
print(basheer)

# enter  the number: 3
# 14
# enter the number: 5
# 55    

# Treasure Hunt Guessing Game

f=1
while f<=100:
    n=int(input("enter the number:"))
    if n==7:
        print("Treasure Found!")
        break
    else:
        print("Try Again!")
        
# enter the number: 3
#       Try Again!
# enter the number:5   
#        Try Again! 
# enter the number:5
#        Treasure Found!
        
# Perfect Square Festival  
  
for i in range(1,501):
    if i*i<=500:
        print(i*i,end="")
# 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 484              
     
# Cube Challenge
        
n=int(input("enter the number:"))    
for i in range(1,n+1):
    print(i**3)

# Input:
# 3
# Output:
# 1
# 8
# 27
# Input:
# 5
# Output:
# 1
# 8
# 27
# 64
# 125        


         

        
        