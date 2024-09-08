mat = [[0 for x in range(5)]
        for y in range(5)]

count = 0
for r in range(5):
    for c in range(len(mat[r])):
        print(mat[r][c])
        count += 1

print(count)

