# search.py
# John David Mohr
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """Search the deepest nodes in the search tree first."""

    "Creating stack and getting the initial node"
    frontier = util.Stack()
    searchedNodes = []
    initialState = problem.getStartState()
    nodeHead = (initialState, [])
    frontier.push(nodeHead)

    "Searching the next node in frontier"
    while not frontier.isEmpty():
        state, action = frontier.pop()

        "Appending searched nodes"
        if state not in searchedNodes:
            searchedNodes.append(state)

            if problem.isGoalState(state):
                return action

            else:
                successors = problem.getSuccessors(state)
                "Get successors and push to frontier"
                for nextState, successorAction, successorCost in successors:
                    nextAction = action + [successorAction]
                    nextNode = (nextState, nextAction)
                    frontier.push(nextNode)

    return action

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    "Creating queue and getting the initial node"
    frontier = util.Queue()
    searchedNodes = []
    initialState = problem.getStartState()
    nodeHead = (initialState, [], 0)
    frontier.push(nodeHead)

    "Searching the next node in frontier"
    while not frontier.isEmpty():
        state, action, cost = frontier.pop()

        "Appending searched nodes"
        if state not in searchedNodes:
            searchedNodes.append(state)

            if problem.isGoalState(state):
                return action

            else:
                successors = problem.getSuccessors(state)
                "Get successors and push to frontier"
                for nextState, successorAction, successorCost in successors:
                    nextAction = action + [successorAction]
                    nextCost = cost + successorCost
                    nextNode = nextState, nextAction, nextCost
                    print(nextState, successorAction, successorCost)
                    frontier.push(nextNode)
    return action

    util.raiseNotDefined()

def lowestCostFirst(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    "Creating priority queue and getting the initial node"
    frontier = util.PriorityQueue()

    "*** It took me forever to figure out you needed curly braces instead of square braces***"
    searchedNodes = {}

    initialState = problem.getStartState()
    nodeHead = (initialState, [], 0)
    frontier.push(nodeHead, 0)

    "Searching the next node in frontier"
    while not frontier.isEmpty():
        state, action, cost = frontier.pop()

        if state not in searchedNodes or cost < searchedNodes[state]:
            searchedNodes[state] = cost

            if problem.isGoalState(state):
                return action
            else:
                successors = problem.getSuccessors(state)
                "Get successors and push to frontier"
                for nextState, successorAction, successorCost in successors:
                    nextAction = action + [successorAction]
                    nextCost = cost + successorCost
                    nextNode = (nextState, nextAction, nextCost)

                    frontier.update(nextNode, nextCost)

    return action

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    "Creating priority queue and getting the initial node"
    frontier = util.PriorityQueue()
    searchedNodes = []
    initialState = problem.getStartState()
    nodeHead = (initialState, [], 0)
    frontier.push(nodeHead, 0)

    "Searching the next node in frontier"
    while not frontier.isEmpty():
        state, action, cost = frontier.pop()
        node = (state, cost)
        searchedNodes.append((state, cost))

        if problem.isGoalState(state):
            return action

        else:
            successors = problem.getSuccessors(state)

            "Get successors and push to frontier and setting searched status"
            for nextState, successorAction, successorCost in successors:
                nextAction = action + [successorAction]
                nextCost = problem.getCostOfActions(nextAction)
                nextNode = (nextState, nextAction, nextCost)
                searched = False

                for search in searchedNodes:
                    searchState, searchCost = search
                    "If the search cost is greater than the search state push next node to frontier"
                    if (nextState == searchState) and (nextCost >= searchCost):
                        searched = True

                if not searched:
                    frontier.push(nextNode, nextCost + heuristic(nextState, problem))
                    searchedNodes.append((nextState, nextCost))

    return action

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
lcf = lowestCostFirst
astar = aStarSearch
