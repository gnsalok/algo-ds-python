from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        visited = set()
        st = []
        st.append(startNode)
      
        while(st):
            cur = st[-1] # get the top element
            st.pop()

            if(cur not in visited):
                print(cur, end=" ")
                visited.add(cur) #mark visited once here

            for v in self.graph[cur]: # self.graph[v] => list
                if(v not in visited):
                    # visited.add(v) -- dont add visited here... Mistake
                    st.append(v) # these appended vertex need to visited as DFS







g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.DFS(2)  # 2 > 5 > 8 > 6 > 9 > 1

