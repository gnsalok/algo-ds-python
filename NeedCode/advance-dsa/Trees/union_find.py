'''
Union Find (Disjoint Set)

Time complexity : O(m) ; where m in no. of edges

Uses :
- It is used to do cycle detection in graph.
- This Data Structure is utilized in Kruskal's Algorithms.

You can do walkthrough on given Edges -> [[1,2], [4,1], [2,4]]

'''


class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
    
    # look parents of all node
    def printParent(self):
        print(self.par)
        

u = UnionFind(5)
print(u.union(1,2))
print(u.union(2,3))
print(u.printParent())
