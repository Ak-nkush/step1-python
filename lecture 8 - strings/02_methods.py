chai = "masala chaI   " 

print(chai.lower()) 
print(chai.upper())
print(chai.strip()) 
print(chai.replace("masala" , "Ginger"))

s = "lemon , Ginger , masala , mint " 
# this is the string containing the different values seperated by comma and this can be converted a list 

print(s.split()) 
# in this we are split according to the spaces in the string soo has we split from spaces comma are also get split and forms a string 

print(s.split(","))
print(s.split(";"))
# in the given string ; character is not present then it will give the single string in a list format 

t = "masala chai chai " 
print(t.count("chai")) 
print(t.find("masala")) 