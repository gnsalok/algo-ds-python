'''
https://neetcode.io/courses/lessons/python-for-coding-interviews

'''


'''
for range(start, stop, step)
'''

print("---Print reverse list----")
lx = [1,2,3,4,5]
for i in range(len(lx)-1,-1, -1):
    print(lx[i])

print("---Division----")
# division 
print(5//2)


'''
Math
'''

# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-3 // 2)

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-3 / 2))


# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo
import math
from multiprocessing import heap
print(math.fmod(-10, 3))

# More math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))


# ---------------------------
# check array.py