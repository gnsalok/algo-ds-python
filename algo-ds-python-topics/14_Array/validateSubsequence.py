'''
Validate Subsequence in a array.
- Sequence should appear in the same order.

TC : O(N) 
SC : O(1)
'''

def validateSubSequence(arr, sequence):
    arrIdx = 0
    seqIdx = 0
    while(arrIdx < len(arr) and seqIdx < len(sequence)):
        if(arr[arrIdx] == sequence[seqIdx]):
            seqIdx += 1 # this increases only if found match in main arr
        arrIdx += 1 # it will increment and check for match

    if(seqIdx == len(sequence)): # traverse each element in sequence in same order 
        return True 
    return False 
    

arr = [1,2,3,4]
seq = [1,4,3]
print(validateSubSequence(arr, seq))