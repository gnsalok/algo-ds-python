
'''
String Reversal 
'''


def reverse_string(s):
    string = []
    words = s.split(' ')
    print(words)
    for word in words:
        string.insert(0, word)

    return " ".join(string)


s = "i like this program very much"
print(reverse_string(s))
