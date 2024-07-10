'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

TC : 
Union - O(1) - Constant Time
Find - O(n) - Linear
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Union Find - Disjoint Set
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                # path compression 
                par[res] = par[par[res]] 
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            # if both belong to same parent
            if p1 == p2:
                return 0

            # higher rank will be parent
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n

        # every time there is union decrement the connected component, remains will be answer
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res