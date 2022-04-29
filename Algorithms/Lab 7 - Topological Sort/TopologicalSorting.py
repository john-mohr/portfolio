

class TopologicalSorting:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        # file name
        self.name = fileName
        
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

        # sorted list
        self.sortedList = []

    def print_and_save(self):
        #print(self.vertices)
        #print(self.adjacencyList)
        #self.sort()
        self.spider(self.vertices[0], 'F')
        print(self.count)
        with open('count_'+str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(self.count))






    # Topological sorting using decrease-by-one-and-conquer.
    def sort(self):
        # Your code goes here:
        unvisited = self.vertices
        adjacencyDict = self.adjacencyList
        while unvisited:
            for i in self.vertices:
                if self.isSource(i, adjacencyDict):
                    self.sortedList.append(i)
                    unvisited.remove(i)

                    if i in adjacencyDict:
                        del adjacencyDict[i]


    def isSource(self, vertex, adjacencyDict):

        for i in self.vertices:
            if i in adjacencyDict:
                for j in adjacencyDict[i]:
                    if vertex == j:
                        return False
        return True








    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self, start, end):
        # Your code goes here:
        self.count = 0
        unvisited = self.vertices

        for v in self.vertices:
            if v in unvisited:
                unvisited.remove(v)
                self.recurs(v, end, unvisited)

        return self.count

    def recurs(self, vertex, end, unvisited):

        if vertex == end:
            self.count += 1
            return
        else:
            for adj in self.adjacencyList[vertex]:
                if adj in unvisited:
                    self.recurs(adj, end, unvisited)



if __name__ == "__main__":

    #s = TopologicalSorting("graph_example.txt")
    #s.print_and_save()

    # Be careful! graph-courses.txt is incomplete. Please finish this txt file at first. 
    #s = TopologicalSorting("graph_courses.txt")
    #s.print_and_save()

    #s = TopologicalSorting("graph_spider.txt")
   # s.print_and_save()

    s = TopologicalSorting("graph_spider.txt")
    s.print_and_save()