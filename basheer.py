# set=> it is mutable collection of unordered ,finite,unique elements.
set1={1,2,3,"basheer","kiran","srinu"}
print(set1) #set is mainly use in duplication elements.
print(set1)
print(len(set1))
# ex:
list1=[1,1,22,22,'sr1','str2']
print(set(list1))
print(list(set(list1)))
#Frozenset=> it is immutable collection of unordered ,finite,unique elements.
frozenset1=frozenset([1,2,3,'str1',2,3])
print(frozenset1)
print(set(frozenset1))

set1={1,2,3,"basheer","kiran","srinu"}
print(set(set1))
print(frozenset(set1))

#Boolean => True or False
print(2>4)

#None => it is represented as empty elements
a=None
print(type(a))

#variables=> 
#Naming conversions
#Rules

# Name variable properly.Name should convey some meaning
#Rules: 
     #start with these:a-z or A-Z or _
     #Don't start with number
     #No special character._ is allowed
     #Python reserved Keywords 
     
#3 types - snakecase,camelcase,pascal case     
#userinputconfirmpassword
#Pascal case=> UserInputConfirmPassword
#camel case=> userInputConfirmPassword                   ###do not use camel case in python.
#Snake case=> User_Input_Confirm_Password
     
