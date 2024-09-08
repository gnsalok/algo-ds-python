'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

TC : O(E + V)
SC : O (V) - No. of edges
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        visited = set()
        count = 0

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)


        def dfs(node):

            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count




        

        