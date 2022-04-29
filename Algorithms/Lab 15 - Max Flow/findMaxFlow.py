from bridges.bridges import *
import MaxFlow
import sys


def findMaxFlow(inputFile, source, sink):
    # Create a bridges object
    # Modify id and the account information
    bridges = Bridges(151, "YOUR_USER_ID", "YOUR_API_KEY")
    bridges.set_title("Solving Maximum Flow");

    obj = MaxFlow.MaxFlow(inputFile, source, sink)
    print("Max Flow = ", obj.solve())

    # visualizes the last augmenting path found - useful for debugging
    # obj.draw_path()

    # visualizes maximum flow
    obj.draw_maximum_flow()

    g = obj.get_graph()

    # Pass the graph object to BRIDGES
    bridges.set_data_structure(g)
    # visualize the graph
    bridges.visualize()


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage python findMaxFlow.py [input file] [source vertex] [sink vertex]')
        quit()

    findMaxFlow(sys.argv[1], sys.argv[2], sys.argv[3])
