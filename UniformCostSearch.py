'''This Python code implements a Uniform Cost Search (UCS) algorithm to find the optimal solution path from
an initial state to a final state within a graph represented by a set of destinations and their 
connections. It begins by taking inputs for the number of destinations, their names, and the path costs 
between them. Then, it constructs a mapping of each destination to the destinations it can reach along 
with their respective path costs. Using this information, UCS explores nodes based on their cumulative 
path costs, ensuring it always expands the node with the lowest cost. It continues this process iteratively 
until the final state is reached or no more nodes are left to explore. Finally, it prints the optimal 
solution path if found or indicates failure otherwise. The code utilizes classes to represent nodes in the 
graph and employs sorting techniques to manage the fringe efficiently, making it an efficient 
implementation of UCS for finding optimal paths.'''

import numpy as np  # Import numpy library for array operations

class node:  # Define a class 'node' to represent nodes in the graph
    def __init__(self, name=None):  # Constructor method to initialize node attributes
        self.name = name  # Name of the node
        self.action = ""  # Action taken to reach the node
        self.pathCost = ""  # Path cost to reach the node
        self.parent = None  # Parent node of the current node

def isNotPresentInFringe(fringe, a):  # Function to check if a node is not present in the fringe
    for i in fringe:  # Iterate through nodes in the fringe
        if i.name == a:  # Check if node's name matches the given node
            return False  # Return False if node is found in the fringe
    return True  # Return True if node is not found in the fringe

def replaceLow(fringe, c):  # Function to replace node in fringe if a lower path cost is found
    for i in fringe:  # Iterate through nodes in the fringe
        if i.name == c.name:  # Check if node's name matches the given node
            if i.pathCost > c.pathCost:  # Check if current node's path cost is higher than the given node
                i.pathCost = c.pathCost  # Replace the path cost in the fringe with the lower path cost
    return fringe  # Return the updated fringe

def sortFringe(fringe):  # Function to sort fringe based on path cost
    l = len(fringe)  # Get the length of the fringe
    for i in range(l):  # Iterate through nodes in the fringe
        for j in range(l):  # Iterate through nodes in the fringe
            if j > i:  # Ensure only nodes ahead are compared
                if fringe[j].pathCost < fringe[i].pathCost:  # Compare path costs of nodes
                    a = fringe[i]  # Swap nodes if path cost of jth node is smaller
                    fringe[i] = fringe[j]
                    fringe[j] = a
    return fringe  # Return the sorted fringe

def solution(n):  # Function to print the solution path
    if n.parent != None:  # Check if the node has a parent
        solution(n.parent)  # Recursively call the function to print parent nodes
        print(f":{n.action} -> {n.name}", end="")  # Print action and node name
    else:
        print(n.name, end="")  # Print the initial state

nd = int(input("How many destinations are there?: "))  # Input number of destinations

destinations = []  # List to store destination names
print("Enter the name of all destinations:")
for i in range(nd):
    destinations.append(input())  # Input destination names

arr = np.empty([nd, nd], dtype=str)  # Initialize 2D array for path costs

print("Enter the path cost if there is any path in between otherwise '0'")
for i in range(nd):
    for j in range(nd):
        if i == j:
            arr[i, j] = arr[j, i] = "0"  # Set diagonal elements to '0'
        else:
            if arr[i, j] == '':
                option = input(f"{destinations[i]} --> {destinations[j]}: ")
                if option != "0":
                    arr[i, j] = arr[j, i] = option  # Input path cost if exists
                else:
                    arr[i, j] = arr[j, i] = "-"  # Set '-' if no path

map = {}  # Dictionary to store mappings from destinations to reachable destinations
for i in range(nd):
    arr2 = arr[i]
    arrn = []
    arrpc = []
    for j in range(len(arr2)):
        if arr2[j] != "-" and arr2[j] != "0":
            arrn.append(destinations[j])
            arrpc.append(arr2[j])
    map.update({destinations[i]: {"actions": arrn, "pathCost": arrpc}})  # Update dictionary with mappings

fringe = []  # List to store nodes to be explored
explored = []  # List to store explored nodes

start = input("Enter the name of the initial state: ")  # Input initial state
goal = input("Enter the name of the final state: ")  # Input final state

if start == goal:
    print("Your initial and final state are the same!")  # Handle case where initial and final states are the same
else:
    initial = node(start)  # Create initial node
    initial.pathCost = 0  # Set initial path cost to 0
    fringe.append(initial)  # Add initial node to fringe
    flag = 0
    while len(fringe) > 0:
        sortFringe(fringe)  # Sort the fringe based on path cost
        a = fringe.pop(0)  # Remove node with lowest path cost from fringe
        if a.name == goal:  # Check if goal state is reached
            solution(a)  # Print solution path
            flag = 1
            break
        explored.append(a.name)  # Add current node to explored list
        dicti = map.get(a.name)  # Get actions and path costs for current node
        action = dicti.get("actions")
        pc = dicti.get("pathCost")
        for i in range(len(action)):
            child = node(action[i])  # Create child node
            child.action = f"Go({action[i]})"  # Set action for child node
            child.parent = a  # Set parent for child node
            child.pathCost = int(pc[i]) + int(child.parent.pathCost)  # Calculate path cost for child node
            if i not in explored or isNotPresentInFringe(fringe, i):
                fringe.append(child)  # Add child to fringe if not explored or not present in fringe
            else:
                fringe = replaceLow(fringe, child)  # Replace node in fringe if lower path cost is found
    if flag == 0:
        print("Failure")  # Print failure if goal state is not reached