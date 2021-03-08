"""
Problem : Test Given String is Anagram or not?
Author : Alok Tripathi

"""


def check(s1, s2):

    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
