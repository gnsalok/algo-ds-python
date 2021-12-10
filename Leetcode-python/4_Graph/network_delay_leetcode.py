'''
TODO :
network delay time - leetcode 

'''
from collections import defaultdict

class Solution:
    #time -> list[list[int]], size, weight/cost
    def networkDelayTime(self,time, N, K): 
        g = defaultdict(list)

        for u,v,cost in times:
            g[u].append((cost,v))





