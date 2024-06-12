'''
Sets and Maps, similar to stacks and queues, are interfaces that can be implemented using trees. 
Implementing them with trees allows for a O(log n) time for operations.
'''


from sortedcontainers import SortedDict

treemap = SortedDict({'c': 3, 'a': 1, 'b': 2}) # output : SortedDict({'a': 1, 'b': 2, 'c': 3})

print(treemap)