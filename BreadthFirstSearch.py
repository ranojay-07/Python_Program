'''This Python code implements a Breadth-First Search (BFS) algorithm to find a solution path from an 
initial state to a final state within a graph represented by a set of destinations and their connections. 
It begins by taking inputs for the number of destinations, their names, and the existence of paths between 
them. Then, it constructs a mapping of each destination to the destinations it can reach. Using this 
information, BFS systematically explores nodes level by level, starting from the initial state and 
expanding outward. It keeps track of explored nodes and the fringe (nodes to be explored) while searching 
for the final state. The search continues iteratively until either the final state is reached or no more 
nodes are left to explore. Finally, it prints the solution path if found or indicates failure otherwise. 
The code utilizes classes to represent nodes in the graph and employs recursion to print the solution path 
backward from the final state to the initial state.'''

import numpy as np

class node:
    def __init__(self, name=None):
        self.name = name
        self.action = ""  # Initialize action attribute
        self.parent = None  # Initialize parent attribute

def solution(n):
    """This function recursively prints the solution path from the initial state to the final state by 
    tracing back through the parent nodes and printing the actions taken at each step."""
    if n.parent != None:
        solution(n.parent)  # Recursively print solution path
        print(f":{n.action} -> {n.name}", end="")
    else:
        print(n.name, end="")  # Print the initial state

def isNotPresentInFringe(fringe, a):
    """This function checks if a node with a specific name is absent from the fringe list, returning True if it's 
    not present and False otherwise."""
    for i in fringe:
        if i.name == a:
            return False
    return True

nd = int(input("How many destinations are there?: "))  # Take input for the number of destinations

destinations = []
print("Enter the name of all destinations:")
for i in range(nd):
    destinations.append(input())  # Input the names of destinations

arr = np.empty([nd, nd], dtype=str)  # Create an empty 2D array for paths

print("Press '1' if there is any path in between otherwise '0'")
for i in range(nd):
    for j in range(nd):
        if i == j:
            arr[i, j] = arr[j, i] = "0"  # Diagonal elements are set to '0'
        else:
            if arr[i, j] == '':
                option = input(f"{destinations[i]} --> {destinations[j]}: ")
                if option == "1":
                    arr[i, j] = arr[j, i] = option  # Set path if exists
                else:
                    arr[i, j] = arr[j, i] = '-'  # Set '-' if no path

map = {}  # Create a dictionary to store mappings from destinations to reachable destinations
for i in range(nd):
    arr2 = arr[i]
    arr3 = []
    for j in range(len(arr2)):
        if arr2[j] == "1":
            arr3.append(destinations[j])
    map.update({destinations[i]: arr3})  # Update dictionary with mappings

fringe = []  # Initialize fringe list
explored = []  # Initialize explored list

start = input("Enter the name of the initial state: ")  # Input the initial state
goal = input("Enter the name of the final state: ")  # Input the final state

if start == goal:
    print("Your initial and final state are the same!")  # Handle case where initial and final state are same
else:
    initial = node(start)  # Create initial node
    fringe.append(initial)  # Add initial node to fringe
    flag = 0
    while len(fringe) > 0:
        a = fringe.pop(0)  # Remove node from fringe
        explored.append(a.name)  # Add node to explored list
        actions = map.get(a.name)  # Get actions for current node
        for i in actions:
            child = node(i)  # Create child node
            child.action = f"Go({i})"  # Set action for child node
            if i not in explored:
                if isNotPresentInFringe(fringe, i):
                    child.parent = a  # Set parent for child node
                    if child.name == goal:
                        solution(child)  # Print solution path
                        flag = 1
                        break
                    fringe.append(child)  # Add child to fringe
        if flag == 1:
            break
    if flag == 0:
        print("Failure")  # Print failure if goal not reached