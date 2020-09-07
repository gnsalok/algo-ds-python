'''
Problem : Write a program to find common elements between two arrays.
Author : Alok Tripathi

'''

# Function to find common elements


def common_ele(a, b):
    a_set = set(a)
    print(a_set)
    b_set = set(b)
    print(b_set)

    if (a_set & b_set):
        print('Common elements: ')
        print(a_set & b_set)
    else:
        print("No common Found!")


# Driver Method
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    common_ele(a, b)
