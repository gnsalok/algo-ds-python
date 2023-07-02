'''
Global, local and non-local variable in python.
'''

from threading import local


x = "global"

def foo():
    global x   # Keyword
    x = "changes"
    print(x)

       
foo()
print("x outside:", x)