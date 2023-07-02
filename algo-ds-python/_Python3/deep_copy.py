
# importing copy module
import copy
  
# initializing list 1 
li1 = [1, 2, [3,5], 4]
  
  
# using copy for shallow copy  
li2 = copy.copy(li1) 
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(li1) 

print(li1)

print(li2)