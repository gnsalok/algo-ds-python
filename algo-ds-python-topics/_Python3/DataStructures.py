'''
Tuple : Immutable Type
'''
tuple = (1,2,3)
print(tuple)


'''
List
'''
ll = [1,2,3]
ll.remove(1) #remove 1 
ll.pop() # remove last element
print(ll)

'''
Set
'''
xset = {1,2,3,4,4} # Will not hold duplicate value 
print(xset)

set_method = set() # or by python method
set_method.add(1)
print("set >>", set_method)


'''
Hashtable
'''
hash_table = {1:"a", 2:"b"}
print(hash_table[1])