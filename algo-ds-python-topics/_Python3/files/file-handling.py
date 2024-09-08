'''
Modes :-
Character   Meaning
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newlines mode (deprecated)

'''

# Writing into file 
with open("file.txt", "w") as f:
    f.writelines("This is new line..\n")


with open("file.txt", "a") as f:
    f.writelines("This is again new line")


# Reading from file 
with open("file.txt","r") as f:
    data = f.read()
    print(data)