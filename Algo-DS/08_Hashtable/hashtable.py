"""
09_Hashtable implementation in python
"""


def hash_function_str(key, table_size):
    """ Hash function to generate index using string type key """
    ov = 0
    key = str(key)
    for i in range(len(key)):
        ov = ov + ord(key[i])

    print(ov%table_size)


if __name__ == '__main__':
    hash_function_str(33, 11)
    hash_function_str('santos', 11)
