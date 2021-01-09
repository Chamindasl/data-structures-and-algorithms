"""
[21-01-09] 399. Evaluate Division
https://leetcode.com/problems/evaluate-division/
"""
class Graph:

    def __init__(self):
        self.vertices = {}

    def add_edge(self, from_edge, to_edge, weight):
        f = self.vertices[from_edge] if from_edge in self.vertices else Vertex(from_edge)
        t = Vertex(to_edge)
        e = Edge(t, weight)
        f.edges.add(e)
        self.vertices[from_edge] = f


class Vertex:

    def __init__(self, name):
        self.name = name
        self.edges = set[Edge]()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return False


class Edge:

    def __init__(self, to, weigth):
        self.to = to
        self.weight = weigth

    

class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph()
        
        for i in range(len(equations)):
            graph.add_edge(equations[i][0], equations[i][1], values[i])
            graph.add_edge(equations[i][1], equations[i][0], 1/values[i])
        
        
        seen = set()

        def dfs(vertex:Vertex, target, mul):
            if vertex is None: return -1
            if vertex.name == target : return mul
            seen.add(vertex.name)
            re = -1
            for e in vertex.edges:
                if e.to.name not in seen:
                    re = dfs(graph.vertices[e.to.name], target, mul*e.weight)
                    if re != -1: return re
            return re
        
        result = []
        
        for q in queries:
            if q[0] in graph.vertices:
                seen.clear()
                result.append(dfs(graph.vertices[q[0]], q[1], 1))
            else: 
                result.append(-1)
        
        return result
