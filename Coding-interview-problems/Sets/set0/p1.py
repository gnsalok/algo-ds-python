

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


if __name__ == "__main__":
    print(fact(5))
