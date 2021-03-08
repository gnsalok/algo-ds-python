'''
Problem : Group anagram array problem
Author : Alok Tripathi

'''


def groupAnagrams(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]

    return list(result.values())


if __name__ == "__main__":

    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
