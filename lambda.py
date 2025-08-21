#lambda function






#higher order functions
# most of the cases lambda functions are used in higner order function
# map, filter and reduce

#1.map
def square(x):
    return x**2
print(list(map(square,[2,3,4])))


#filter function
# it is used to filter to required elements and others ignored
# syntax of filter(filter,iterable)
# def funct(x):
#     return x
print(list(map(lambda x:x*2,[1,23])))
print(list(filter(lambda x:x%2==0,[1,2,3,4,55,6])))
print(list(filter(lambda x:x%2==0 or x%5==0,[1,2,4,6,5,10,55])))


#reduce function
from functools import reduce
print(reduce (lambda x,y:x+y,[1,2,3,4,5,6,7,8,9]))

list1=["basheer","sai"]
print(reduce(lambda x,y:x+y,list1))
print(reduce(lambda x,y: x if x>y else y,[1,2,3]))

def even(x):
    return True if x%2==0 else False
# a=even(5)
print(even(6))