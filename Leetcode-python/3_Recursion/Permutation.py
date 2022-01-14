def getPermutations(arr):
    permutations = []
    permutationHelper(arr, [], permutations)
    return permutations


def permutationHelper(arr, currentPermutation, permutations):
    if not len(arr) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(arr)):
            newArray = arr[:i] + arr[i+1:]
            print("new arr",newArray)
            newPermutation = currentPermutation + [arr[i]]
            print(newPermutation)
            permutationHelper(newArray, newPermutation, permutations)


arr = [1,2,3]
print(getPermutations(arr))