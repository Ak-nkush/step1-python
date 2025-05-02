import copy 
l1 = [1,2,3] 
l2 = copy.copy(l1) 

h1 = [1,2,[33,44]] 
h2 = copy.deepcopy(h1)
# deepcopy is use to create the copy of nested list 

print(l1)
print(l2)
print(h1)
print(h2)