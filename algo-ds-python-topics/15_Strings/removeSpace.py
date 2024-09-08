'''
My    Name is     Alok >>> My Name is Alok

'''

def removeSpace(str):
    newString = " "
    return newString.join(str.split())
    # print("Without extra spaces: ", re.sub(' +', ' ', text1))  # using regular expression




if __name__ == "__main__":
    str = "My    Name is     Alok"
    print(removeSpace(str))