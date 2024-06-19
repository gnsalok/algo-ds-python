'''
https://leetcode.com/problems/course-schedule/

TC : O(N + P) ; where N is no. of course and P in pre-requisite
'''


import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        # Why we need to interate over all all the crs ; because there might be possibility that graph is not connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
