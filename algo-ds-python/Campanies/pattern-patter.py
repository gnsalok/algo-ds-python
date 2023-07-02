
'''
Given a string where each character is a sign ('<', '>', '=') and length of the string is N. You need to insert N+1 positive integers such that the sequence is valid. You are allowed to take positive integers in the range [1, P]. k.
Examples -

Input: <<<
Output: 4 (the sequence can be 1 < 2 < 3 < 4)
Input: <=>
Output: 2 (the sequence can be 1 < 2 = 2 > 1)

https://leetcode.com/discuss/interview-question/1392946/Intuit-or-SDE-2-or-Onsite

'''

def print_patter(s):
    mini = float('inf')
    i = 1 # start with 1
    ans = [i]
    for c in s:
        if c == "=":
            ans.append(i)
        elif c == "<":
            i += 1
            ans.append(i)
        else:
            i -= 1
            ans.append(i)
        mini = min(mini, i)
    
    if mini > 0:
        return max(ans)
    diff = 1 - mini 
    # adjust each number with diff to make all > 0
    return max(map(lambda x: x + diff, ans))


result = print_patter(['<', '=', '>'])
print(result)