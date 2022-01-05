from collections import defaultdict

dl = defaultdict(list)

dl[1].append(1)
dl[1].append(2)

print(dl)

for key in dl:
    for listValue in dl[key]:
        print(key, listValue)