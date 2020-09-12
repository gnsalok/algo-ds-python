"""
@author : Santosh Pillai
@email : santosh.pillai98@gmail.com

"""

class Graph:
    
    def __init__(self, graph_dict=None):
        """ Initializing the graph object. """
        if graph_dict is None:
            graph_dict = {}

        self.__graph_dict = graph_dict

    
    def vertises(self):
        """ return the vertices of the graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ Return all the edges of the graph """
        return self.__generate_edges()

    def __generate_edges(self):
        """generate all the edges from the graph """
        edges = []
        for vertex in self.__graph_dict:
            for neighbours in self.__graph_dict[vertex]:
                if {neighbours, vertex} not in edges:
                    edges.append({vertex, neighbours})

        return edges

    def add_vertex(self, vertex):
        """ if vertex not present in the dict, add it """
        if vertex not in self.__graph_dict.keys():
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):

        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            if vertex2 not in self.__graph_dict[vertex1]:
                self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = vertex2


    def find_path(self, start, end, path=None):
        """ find path from start to end node """
        if path is None:
            path = []
           
        path = path + [start]
        #path.append(start)
        #path.extend([start])
        if start == end:
            return path

        if start not in self.__graph_dict.keys():
            return None

        for node in self.__graph_dict[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    return newpath
        return None

    def find_all_paths(self, start, end, path=None):
        """ Find all the paths between start and end vertices"""
        if path is  None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.__graph_dict.keys():
            return []

        paths= []
        for node in self.__graph_dict[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                print(newpaths)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def vertex_degree(self, vertex):
        """Degree of vertex is the number of adjacent vertices. Loops are
        counted twice """
        adj_vertices  = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res+= str(k) + ' '
        res += '\nedges'

        for edge in self.__generate_edges():
            res += str(edge) + ' '

        return res 


            

if __name__ == '__main__':

     g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
      }

     graph = Graph(g)
     
     print(graph)
     graph.add_edge(('f','c'))
     print(graph.vertises())
     print(graph.edges())
     
     print(graph)
     
     print(graph.find_path('a', 'e'))
     print(graph.find_path('c', 'c'))
     print(graph.find_path('a', 'f'))
     print(graph.find_path('f', 'c'))
     print('*** all paths **')
     print()
     print(graph.find_all_paths('a', 'b'))
     print(graph.vertex_degree('a'):)
