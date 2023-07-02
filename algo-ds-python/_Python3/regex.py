import re

str = "My     Name is Alok"

# Method 1
newStr = re.sub(r"\s+", " ", str)
print(newStr)   

# Method 2
anotherNewStr = " "
print(anotherNewStr.join(str.split()))

# Method 3
def compactStr(str):
    os = ""
    for c in str:
        if c != " " or (os and os[-1] != " "):
            os += c
    return os 

print(compactStr(str))