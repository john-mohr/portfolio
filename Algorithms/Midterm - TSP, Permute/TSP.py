"""John David Mohr"""

def permute(elements, n):

    if n-1 == 0:
        ele = [elements[0],elements[1],elements[2],elements[3],elements[4]]
        permutations.append(ele)

    else:
        for i in range(0,n):
            permute(elements,n-1)

            if n%2 == 1:
                temp = elements[0]
                elements[0] = elements[n-1]
                elements[n-1] = temp

            else:
                temp = elements[i]
                elements[i] = elements[n-1]
                elements[n-1] = temp


def readFile(dict,list):

    with open('vt.txt') as f:
        line = f.readline()

        while line:
            line = f.readline()
            line.replace(" ","")

            if line == "EOF":
                break

            cost = line[line.index("=")+1:len(line)-1]
            src_dst = line[0:line.index("=")]
            dict.update({src_dst: cost})
            town = src_dst[0:src_dst.index("-")]

            if town not in list:
                list.append(town)

def findShortestPath(perms):

    shortest = 10000
    route = None

    #Looking at all permutations, finding the total distance, and then printing the shortest distance with its path
    for i in perms:
        totalDistance = 0
        for j in range(len(i)-1):
            totalDistance += int(routecost.get(i[j]+"-"+i[j+1]))
        totalDistance += int(routecost.get(i[4]+"-"+i[0]))
        if totalDistance < shortest:
            shortest = totalDistance
            route = i
    print(shortest, route)

def run():

    #Reading from text file, creating a dictionary of source and destination cost, and creating a list of towns
    readFile(routecost, towns)

    #Creating all possible permutations of the different routes
    permute(towns, len(towns))

    #Finding and printing the shortest path
    findShortestPath(permutations)


if __name__ == '__main__':

    #global variables
    routecost = {}
    towns = []
    permutations = []

    #running the entire program
    run()

