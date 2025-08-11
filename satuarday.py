# operators:
# arithmatic operator => +,-,*,/,%,//,**,
# assignment operator => =,+=,-=,*=
# relational operator => <,>,>=,<=,!=,==
# logical operator => and,or,not
# bitwise operator=> &,|,^,~,<<,>>
# membership operators=> in,not in
# identity operator=>
# terinory operator=>



#1. Arthimatic operator:
   # BODMAS rule 
#print(2+3*5)
#print((2+3)*5)   

#/,//,%

#num1,num2=1.5,0
#(num1//num2)

#2. Assignement operator:
#

# relational operator:
#

#membership operator => in ,not in
# print(3 in(1,2,3)) 
# print(int('3') not in (1,2,3))
# print(bool(3) in (1,2,3))

# set={1:'1',
#      2:'2',
#      3:'3'}
# print('1' in set)

# logical operator=> or ,and,not
# print(True and False)
# print(True and True)
# print(2 and 3)
# print(0 and 3)
# print(''and [3])

#if 1st input is True then the output is depend on second input.
#if 1st input if false then the output depend on first input itself.
#falses value represented as 0,empty('',(),[],{}).
# or
# print(True or False)
# print(True or True)
# print(2 or 3)
# print(0 or 3)
# print(''or [3])
# print('' or {})
# print('' or [])
# print('Truth' or 'Dare')

#if two values are falsy then it is automatically print the second value itself.
#if two values are truthy then it is printon first value itself.

#not
# print(not True)
# print(not False)

# # Bitwise operator=> &,|,^,>>,<<
# print(5 & 7)
# # number are written as bitwise type like " 0011"
# # and
# print(2&3)
# #or
# print(bin(5)[2:])
# print(oct(11))
# print(hex(7))
# print(int(0b111))
# print(0b111)
# print(13 | 22)
# a=13
# b=22
# print(bin(a))
# print(bin(b))

#xor=>'^' 
# print(13 ^ 22)

# control statements
#1. conditional statements:if,else,ifelse
# indendation

#n=int(input('enter the numbers:'))
#if n%2==0:
 #      print("even number")
#else:
#   print('odd value')       
   
#n=int(input("enter the value:"))   
#if n>=0:
#       print("positive")
#else:
#   print("negative")       

# nested if.

# n=int(input("enter the value:"))
# if n>0:
#        print("positive")
# else:
#    if n==0:
#       print("zero")
#    else:
#       if n==-1:
#          print("negative of 1")  
#       else:
#          print("negative")        

#elif statement:
 
# num1 =-1
# if num1>0:
#        print("positive")
# elif num1==0:
#    print("zero")
# elif num1== -1:
#    print("-1")
# else:
#    print("negative")             

# num1=float(input("enter the number1:"))
# num2=float(input("enter the number2:"))
# symbol=input("enter the symbol:")
# if symbol is "+":
#        print(num1 + num2)
# elif symbol is "-":
#        print(num1 - num2)   
# elif symbol is "%":
#        if num2 !=0: # it is used to avoid zero division error.
#               print(num1 % num2)
#        else:
#               print("it is possible")
# else:
#    print("basheer")

# question for practice:  we should write less than to greater than:
# n=int(input("enter the units:"))
# if n >= 300:
#        print(n*4) 
# else:
#        if n>=200:
#               print(n*3)
#        else:
#               if n>=100:
#                      print(n*2)
#               else:
#                      if n>=0:
#                             print(n*0)
#                      else:
#                             print("basheer")  

# year=int(input("enter the year:"))
# if year %400==0 or (year%100 !=0 and year%4==0):
#        print('leap')
# else:
#        print("not leap")
       
                                                 