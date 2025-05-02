
x = 12 + 12 
print("x:" , x) 
y = 2.5 * 4 
print("y:",y) 
z = 2 ** 100 
print("z:",z) 


import math 
print(math.pi)
#todo -  The math module is part of the Python standard library, meaning it's built-in and always available for use.

import random 
random.random() 
# it gives the random value 

random.choice([1,2,3,4,5])
# randomly gives the number from the array 

username = "chaiAurcode"
len(username) 
# it gives the size of the string 

username[0] 
# it behaves as list internally 
# indexing start from 0 from left and -1 from right 

#! username[0] = 'A' 
#! it will gives the error as string is immutable 

username[1:3] 
# its a slicing method of string here last specified index i.e 3 is not include

dir(username) 
# it provides the all available method for a datatype 

mylist = [123 , "chai" , 3.14 ]
print(mylist) 
print(len(mylist)) 
# here the length of list start from 1 that a human readable format 
# here also indexing start from 0 from left and -1 from right 

mydict = {'one' : 'lemon',
        'two' : 'ginger' ,
        'comic' : 'naagraj'}
print(mydict) 
print(mydict['comic']) 
# error - keyerror - if key is not present in the dictionary 

myTup = (1,2,3) 
# here also we can access element through indexing 
print(myTup)
print(len(myTup)) 
#  mostly it is not preferrable 
