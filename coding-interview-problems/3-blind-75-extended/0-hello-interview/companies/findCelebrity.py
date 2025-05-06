

'''
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
 
Explanation : There are three people numbered 0, 1, and 2. graph[i][j] = 1 means that person numbered i knows person numbered j, 
and graph[i][j] = 0 means that person numbered i does not know person numbered j. 
The "celebrity" is person numbered 1, because both 0 and 2 know him/her, but 1 does not know anyone.

'''


def findCelebrity(graph):
    n = len(graph)
    candidate = 0

    for i in range(1, n):
        if graph[candidate][i] == 1:
            candidate = i

    for i in range(n):
        if i != candidate and (graph[candidate][i] == 1 or graph[i][candidate] == 0):
            return -1

    return candidate


mat = [
    [1,1,0],
    [0,1,0],
    [1,1,1]
]

print(findCelebrity(mat)) # 1