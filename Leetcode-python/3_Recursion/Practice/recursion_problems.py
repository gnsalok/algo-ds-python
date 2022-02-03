
'''
Sum of number from 1 to n

return 1 + 2 + 3 + 4 + .... + (n-1) + n
'''

# # TRUST the function 
# def sum_n(n):
#     if(n == 1): # Or base case could be 0 --> return 0
#         return 1

#     left_part = sum_n(n-1)
#     print(f"Left Part is {left_part}")
#     return left_part + n

    

'''
Sum of Digit of the number 

INPUT  : 12344
OUTPUT : 1 + 2 + 3 + 4 +    5       = 15

1234  + 5

'''

def digit_sum(n):
    if(n == 0):
        return 0
    last_digit  = n % 10
    remaining_part = n // 10
    return digit_sum(remaining_part) + last_digit



if __name__ == "__main__":
    # result = sum_n(10)

    result = digit_sum(12345)
    print(result)
    