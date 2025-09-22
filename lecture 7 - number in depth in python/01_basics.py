x = 2 
y = 3 
z = 4 
sum = x + y  
print("Printing the sum : ",x)
power = x**2 
print("printing power :" ,power)

cal = x + y * z 
# this thing is ok according to the theory but in real world production we use parenthesis , as parenthesis has highest priority 
cal = (x+y)*z 


f = 40 + 2.23 
# python provide higher precision , but this kind doesn't works in production it is preferred to have both the dataype should be of same datatype 
# because in future there can be mistake such as "hitesh"+ 3 , which cause the error in the code base 

# typecasting 
f = 40 + int(2.23) 
# here we can see both are of same datatype 

# operator overloading 
joint = 'chao' + 'chai' 
print("cancatenation : " , joint)
# operator decide by itself to perform the operation according to datatype , this is called as cancatenation 

# precision control 
result = 1/3.0
print(result)


print(1<2)
# it gives the result as true internally it is 1 thats a integer 
print(x,y,z)

print(x<y<z)
# it is the short hand for x<y and y<z 

print(1 == 2<3)
# 1 == 2 and 2<3  
