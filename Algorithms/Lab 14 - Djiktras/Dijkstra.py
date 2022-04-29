"""
    Dijkstra.py
    Implementation of Dijkstra's algorithm for the shortest path problem for a positive-weighted graph

    [John David Mohr]
"""

from bridges.graph_adj_list import *
import heapq

class Dijkstra():
    def __init__(self, inputFile, startingVertex, goalVertex):
        # an initially empty dictionary containing mapping: vertex: [child, weight]
        self.adjacency = {}
        # collection of vertices
        self.vertices = []
        # each dictionary entry contains mapping of vertex:parent
        self.parent = {}
        # startingVertex, goalVertex
        self.startingVertex, self.goalVertex = startingVertex, goalVertex

        # The following reads in the input file and constructs an adjacency list of the graph.
        graph = open(inputFile)
        for line in graph:
            entry = line.split()

            # get the vertices
            self.vertices.append(entry[0])
            self.vertices.append(entry[1])

            if entry[0] not in self.adjacency:
                self.adjacency[entry[0]] = []

            # construct an edge for the adjacency list
            edge = (entry[1], int(entry[2]))
            self.adjacency[entry[0]].append(edge)

        # remove duplication in vertices
        self.vertices = list(set(self.vertices))

        # checking if start and goal are in vertices
        if startingVertex not in self.vertices:
            print('Starting vertex', startingVertex, 'not present in graph')
            quit()
        elif goalVertex not in self.vertices:
            print('Goal vertex', goalVertex, 'not present in graph')
            quit()

        # create Bridges graph
        self.g = GraphAdjList()
        for vertex in self.vertices:
            self.g.add_vertex(vertex, str(vertex))
            self.g.get_visualizer(vertex).color = "red"
        
        for vertex in self.adjacency:
            unvisited = vertex
            for edge in self.adjacency[vertex]:
                self.g.add_edge(vertex, edge[0], edge[1])

    # solve it using Dijkstra algorithm
    def loop(self):
        for adj in self.adjacency[self.startingVertex]:
            print(adj[0], adj [1])

    def solve(self):
        # your code goes here:
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[self.startingVertex] = 0
        vertexQ = []
        heapq.heappush(vertexQ, [0,self.startingVertex, None])
        visited = []
        path = []
        while len(vertexQ) > 0:
            currD,currV,parent = heapq.heappop(vertexQ)

            if currV not in visited:
                visited.append(currV)
                path.append((currV, parent))

                if currV == self.goalVertex:
                    self.path = path
                    return

                for adjacency in self.adjacency[currV]:
                    neighbor = adjacency[0]
                    weight = adjacency[1]
                    distance = currD + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(vertexQ, [distance, neighbor, currV])

    # retrieve the path from start to the goal 
    def find_path(self):
        # your code goes here:
        path = dict(self.path)
        self.path = []
        self.path.append(self.goalVertex)

        node = self.goalVertex
        while int(node) != int(self.startingVertex):
            node = path[node]
            self.path.append(node)

    # draw the path as red
    def draw_path(self):
        self.path = self.path[::-1]
        for i in range(len(self.path)-1):
            self.g.get_link_visualizer(self.path[i], self.path[i+1]).color = "red"


    # return the Bridges object
    def get_graph(self):
        return self.g
