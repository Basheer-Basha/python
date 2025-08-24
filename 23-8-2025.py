#built-in function
#case conversion-builtin function
#string 

#lower
#it is used to convert upper to lower
a="BASHeer"
b=a.lower()
print(b)

#or 
a="BASHEER"
print(a.lower())

#upper
#it is used to lower to upper
a="basheer"
print(a.upper())

#isupper
a="basheer"
print(a.isupper())
a="BASHEER"
print(a.isupper())

#islower
a="BASHEER"
print(a.islower())
b=a.lower()
print(b.islower())

#swapcase
#it is used to change upper to lower and lower to upper
a="basHEER"
print(a.swapcase())

#capitalize
# it is used to print first character is capital
a="basheer basha"
print(a.capitalize())

#title
#it is used to overcome the capitalize and it is print first word as captital for every letter.
a="basheer basha"
print(a.title())

#trimming and replacing built in fun
#strip
#it is used to delete the special character
a="  basheer  "
print(a.strip())

#lstrip
a="  basheer   b"
b=a.lstrip()
print(b)

#rstrip
a="  basheer  "
b=a.rstrip()
print(b)

#replace
#it is used to replace the word to new word
a="Basheer is learning java"
b=a.replace("java","python")
print(b)

c=a.replace("to","buy")
print(c) #Basheer is learning java

#find
#it is used to find the number or character in the string
a="basheer"
print(a.find("e")) #4

#startswith
a="basheer"
print(a.startswith("b")) #True
print(a.startswith("B")) #False

#endswith
a="basheer basha"
print(a.endswith("a")) #True
print(a.endswith("A")) #False

#split
a=input("enter the number:")
print(a.split(",")) #["2","3","653"]

#map function
a=num1,num2,num3=list(map(float,input("enter the numbers:").split(",")))
print(a)
# or
def map1(x):
    return(x*x)
print(list(map(map1,[1,2,3])))

#join
list1=["1","2","3","4","basheer"]
str1=",".join(list1)
print(str1)

#set 
#add
a={1,2,3}
a.add(4)
print(a)

#remove
a={1,2,5,2,6,26}
a.remove(2)
print(a)
a.remove(26)
print(a)


#discard
a={1,54,36,587}
a.discard(13)
print(a)

#pop
a={1,2,3}
a.pop()
print(a)

#clear
a={1,3,232,423}
print(a.clear())

#union
a={1,2,3,4,5}
b={1,4,2,45,3}
print(a.union(b))
print(b.union(a))

#difference
a={1,2,5,4,54,43,6,454,}
b={3,2,12,11,23,231,}
print(a.difference(b))
print(b.difference(a))

#intersection
a={1,2,3,4}
b={2,3,1,5,7,8}
print(a.intersection(b))

#symmetric_differences
a={1,2,3,4,7,8,}
b={2,3,56,742,234}
print(a.symmetric_difference(b))

#isdis_joint
a={1,2,3}
b={1,2,10,11,12}
print(a.isdisjoint(b))




