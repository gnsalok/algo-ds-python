ls = "sts"
temp = ""

for c in range(len(ls)-1, -1, -1):
    temp += ls[c]
    
if(temp == ls):
    print("Palindrome")
else:
    print("not")
