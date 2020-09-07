'''
Problem : Minimum number of Appends needed to make a string palindrome

'''

# Checking if the String is palindrome or not


def isPalindrome(Str):
    Len = len(Str)

    # single character is always palindrome
    if (Len == 1):
        return True

    # pointing to first character
    ptr1 = 0
    # pointing to last character
    ptr2 = Len - 1

    while (ptr2 > ptr1):
        if (Str[ptr1] != Str[ptr2]):
            return False
        ptr1 += 1
        ptr2 -= 1
    return True

# Recursive function to count number of appends


def noOfAppends(s):
    if (isPalindrome(s)):
        return 0

    # Removing first character of String by
    # incrementing base address pointer.
    del s[0]
    return 1 + noOfAppends(s)


if __name__ == "__main__":
    se = "abede"
    s = [i for i in se]
    print(noOfAppends(s))
