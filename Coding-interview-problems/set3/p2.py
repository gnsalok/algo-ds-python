# find duplicate char in string


check_string = "Alllok"

count = {}
for s in check_string:
    if s in count:
        count[s] += 1  # string is key and inc no. is value
        print(count)
    else:
        count[s] = 1

for key in count:
    if count[key] > 1:  # if value will greater then 1 means it's duplicate 
        print(key, count[key])
