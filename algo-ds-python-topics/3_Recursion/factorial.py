def print_factorial(n):
    if n == 0 : #base 
        return 1
    else:
        return n * print_factorial(n-1)


if __name__ == "__main__":
    result = print_factorial(6)
    print(result)

