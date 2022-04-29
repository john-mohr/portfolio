"""
    MaxFlow.py
    Implementation of the shortest augmenting path algorithm for calculating maximum flow

    [YOUR NAME GOES HERE]
"""
from bridges.graph_adj_list import *

class MaxFlow():
    def __init__(self, inputFile, source, sink):
        # an initially empty dictionary of forward edges containing mapping: vertex: [child, edge capacity]
        self.adjacency = {}
        # an initially empty dictionary of backward edges containing mapping: child: [vertex, edge capacity]
        self.backwards = {}
        # collection of vertices
        self.vertices = []
        # source, sink
        self.source, self.sink = source, sink
        # flow network
        self.maxFlow = 0
        self.flow = {}

        # The following reads in the input file and constructs an adjacency list of the graph.
        graph = open(inputFile)
        for line in graph:
            entry = line.split()

            # get the vertices
            self.vertices.append(entry[0])
            self.vertices.append(entry[1])

            if entry[0] not in self.adjacency:
                self.adjacency[entry[0]] = []
            if entry[1] not in self.backwards:
                self.backwards[entry[1]] = []

            # construct an edge for the adjacency list
            forwardEdge = (entry[1], int(entry[2]))
            self.adjacency[entry[0]].append(forwardEdge)
            backwardEdge = (entry[0], int(entry[2]))
            self.backwards[entry[1]].append(backwardEdge)
            self.flow[entry[0], entry[1]] = 0

        # remove duplication in vertices
        self.vertices = list(set(self.vertices))

        # checking if source and sink are in vertices
        if source not in self.vertices:
            print('Source', source, 'not present in graph')
            quit()
        elif sink not in self.vertices:
            print('Sink', sink, 'not present in graph')
            quit()

    # solve the maximum flow by repeatedly finding the shortest augmenting path
    def solve(self):
        labeled = {}
        labeled[self.source] = (float('inf'), None, None)
        queue = []
        queue.append(self.source)

        while queue:
            i = queue.pop(0)
            # forward edges

            for vertex in self.adjacency[i]:
                # your code goes here:
                j = vertex[0]
                jflow = vertex[1]

                if j not in labeled:
                    AvailCap = jflow - self.flow[(i,j)]

                    if AvailCap > 0:
                        lj = min(AvailCap, labeled[i][0])
                        labeled[j] = (lj, i, "+")
                        queue.append(j)

            # backward edges
            if i in self.backwards:
                for vertex in self.backwards[i]:
                    # your code goes here:
                    j = vertex[0]
                    jflow = vertex[1]
                    if j not in labeled:

                        if jflow > 0:
                            lj = min(labeled[i][0], jflow)
                            labeled[j] = (lj, i,"-")
                            queue.append(j)

            if self.sink in labeled:
                # augment along the augmenting path found
                # your code goes here:
                self.path = []
                j = self.sink
                flow = labeled[self.sink][0]
                while j != self.source:
                    if labeled[j][2] == "+":
                        self.flow[(labeled[j][1],j)] = self.flow[(labeled[j][1],j)] + flow
                    else:
                        self.flow[(j,labeled[j][1])] = self.flow[(j,labeled[j][1])] - flow
                    self.path.append(j)
                    j = labeled[j][1]

                self.path.append(self.source)
                labeled = {}
                labeled[self.source] = (float('inf'), None, None)
                queue = []
                queue.append(self.source)

                # print current flow and shortest augmenting path for this iteration
                print(flow, ":", self.path[::-1])
                # increase max flow by current flow
                self.maxFlow += flow

        return self.maxFlow

    # draw last augmenting path
    # forward edges in green
    # backward edges in orange
    def draw_path(self):
        # create Bridges graph
        self.g = GraphAdjList()
        for vertex in self.vertices:
            self.g.add_vertex(vertex, str(vertex))
            self.g.get_visualizer(vertex).color = "red"

        for vertex in self.adjacency:
            for edge in self.adjacency[vertex]:
                self.g.add_edge(vertex, edge[0], edge[1])

        for i in range(len(self.path) - 1):
            # draw green forward edges
            if self.g.get_edge(self.path[i], self.path[i + 1]):
                link = self.g.get_link_visualizer(self.path[i], self.path[i + 1])
                link.color = "green"
            # draw orange backward edges
            else:
                link = self.g.get_link_visualizer(self.path[i + 1], self.path[i])
                link.color = "orange"
            link.thickness = 3.0

        # draw last augmenting path
        # forward edges in green
        # backward edges in orange

    def draw_maximum_flow(self):
        # create Bridges graph
        self.g = GraphAdjList()
        for vertex in self.vertices:
            self.g.add_vertex(vertex, str(vertex))
            self.g.get_visualizer(vertex).color = "red"

        for vertex in self.adjacency:
            for edge in self.adjacency[vertex]:
                self.g.add_edge(vertex, edge[0])
                link = self.g.get_link_visualizer(vertex, edge[0])
                link.label = str(self.flow[vertex, edge[0]]) + "/" + str(edge[1])
                link.thickness = 2.0

    # return the Bridges object
    def get_graph(self):
        return self.g
