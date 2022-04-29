"""
    Graph.py
    Implementation of graph traversal algorithms

    [John David Mohr, CK Padayao]
"""

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graph_file = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacency_list = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graph_file:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (first_vertex, second_vertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(first_vertex)
            self.vertices.append(second_vertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if first_vertex not in self.adjacency_list:
                self.adjacency_list[first_vertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacency_list[first_vertex].append(second_vertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacency_list:
            self.adjacency_list[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFS_init(self):
        # initially all vertices are considered unknown
        self.unvisited_vertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFS_init()
        if method is 'recursive':
            # Your code goes here:
            for v in self.adjacency_list:
                if v in self.unvisited_vertices:
                    self.DFS_recursion(v)

            return self.path

        elif method is 'stack':
            for v in self.adjacency_list:
                if v in self.unvisited_vertices:
                    self.DFS_stack(v)

            return self.path
            

    def DFS_recursion(self, vertex):
            self.path += vertex
            self.unvisited_vertices.remove(vertex)
            for adj in self.adjacency_list[vertex]:
                if adj in self.unvisited_vertices:
                    self.DFS_recursion(adj)

    def DFS_stack(self, vertex):
        stack=[]
        stack.append(vertex)
        while bool(stack):
            v = stack.pop()
            if v in self.unvisited_vertices:
                self.unvisited_vertices.remove(v)
                self.path += v
                for adj in self.adjacency_list[v]:
                    if adj in self.unvisited_vertices:
                        stack.append(adj)

    def BFS_init(self):
        # initially all vertices are considered unknown
        self.unvisited_vertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""


    def BFS(self):
        self.BFS_init()
        for v in self.vertices:
            if v in self.unvisited_vertices:
                self.BFS_queue(v)
        
        return self.path


    def BFS_queue(self, vertex):
        queue = [vertex]

        while queue:
            vert = queue.pop(0)
            if vert in self.unvisited_vertices:
                self.unvisited_vertices.remove(vert)
                self.path += vert
                for adjV in self.adjacency_list[vert]:
                    if adjV in self.unvisited_vertices:
                        queue.append(adjV)


    def has_cycle(self):
        #Creating a boolean list to determine what vertices have been visited
        visited = [False] * len(self.vertices)

        #Iterating through all vertices
        for i in self.vertices:

            #If a vertex has not been visited call the helper function on that vertex
            if visited[self.vertices.index(i)] == False:
                if (self.has_cycle_helper(i, visited, -1, )) == True:

                    return True

        return False


    def has_cycle_helper(self, vertex, visited, parent):
        #Marking current vertex as visited
        visited[self.vertices.index(vertex)] = True

        #Recursively calling the current vertex's adjacent vertices
        for i in self.adjacency_list[vertex]:

            if visited[self.vertices.index(i)] == False:
                if(self.has_cycle_helper(i,visited,vertex)):
                    return True
            #Checking that the vertex is not the vertex's parent
            elif  parent != i:
                return True

        return False


    # Work on this function for at most 10 extra points
    def shortest_path(self, p, q):
        # Your code goes here:
        pass # delete "pass" after writing your own code here 
  
                
        

        

