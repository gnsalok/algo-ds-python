'''
Write a program that prints the numbers from 1 to n. But for multiples of 3, print 'Fizz' instead of the number, 
and for multiples of 5, print 'Buzz'. For numbers that are multiples of both 3 and 5, print 'FizzBuzz'
'''



n = 1

while(n < 21):
    if(n % 3  == 0 and n % 5 == 0):
        print("FizzBuzz")
    elif(n%3 == 0):
        print("Fizz")
    elif(n % 5 == 0):
        print("Buzz")
    else:
        print(n)
    n = n + 1
    

    
