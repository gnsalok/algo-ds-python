from collections import defaultdict

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}



for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)
    adjList[dst].append(src)
print(adjList)


# simple version using defaultdict(list)
# graph = defaultdict(list)
# for src, dst in edges:
#     graph[src].append(dst)
#     graph[dst].append(src)
# print(graph.values())
