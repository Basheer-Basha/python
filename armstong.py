#method-1:
n=int(input("enter the number:"))
n1=n
sum=0
for i in range(1,n+1):
    rem=n%10
    sum+=rem**len(str(n1))
    n=n//10   
print(sum)    
if sum==n1:
    print("arm strong number")
else:
    print("not armstrong number")
# method-2:   
n=int(input("enter the number:")) 
n2=n
sum=0
while n>0:
    rem=n%10
    sum+=rem**len(str(n2))
    n=n//10
print(sum)    
if sum==n2:
    print("armstrong")    
else:
    print("not")
    
# method-3:    
def armstrong(n):
    n2=n
    sum=0
    for i in range(1,n+1):
        rem=n%10
        sum+=rem**len(str(n2))
        n=n//10
    print(sum)   
    if sum==n2:
        print("arms") 
    else:
        print("not")           
    
n=int(input("enter the number"))    

armstrong(n)

