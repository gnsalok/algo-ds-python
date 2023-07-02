''''
9 => 1001  :: Max gap = 2
1001 -> 2
100001 -> 4
1000010001 -> 4

'''

def binaryGap(N):
    N = bin(N)[2:]
    b = 0
    maxb = 0

    for k in N:
        if(int(k) == 0):
            b += 1
        elif(int(k) == 1):
            maxb = max(b, maxb)
            b = 0
    return maxb


val = binaryGap(32)
print(val)