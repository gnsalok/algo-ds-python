# expand in both directions of low and high to find all palindromes
def expand(str, low, high, s):

    # run till str[low.high] is a palindrome
    while low >= 0 and high < len(str) and str[low] == str[high]:

        # push all palindromes into the set
        s.add(str[low : high + 1])

        # expand in both directions
        low = low - 1
        high = high + 1


# Function to find all unique palindromic substrings of given String
def allPalindromicSubStrings(str):

    # create an empty set to store all unique palindromic substrings
    s = set()

    for i in range(len(str)):

        # find all odd length palindrome with str[i] as mid point
        expand(str, i, i, s)

        # find all even length palindrome with str[i] and str[i+1]
        # as its mid points
        expand(str, i, i + 1, s)

    # print all unique palindromic substrings
    print(s, end="")


if __name__ == "__main__":

    str = "google"
    allPalindromicSubStrings(str)
