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
    if count[key] > 1:
        print(key, count[key])
