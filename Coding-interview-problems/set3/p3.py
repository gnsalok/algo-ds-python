"""
Problem : Test Given String is Anagram or not?
Author : Alok Tripathi

"""


def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()

    return (list_str1 == list_str2)


print(is_anagram('surya', 'suray'))
