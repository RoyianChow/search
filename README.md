# search
ex1
BFS Search 
This program performs a breadth-first search (BFS) on a given graph to find a path between a starting node and a goal node.

Usage
Define the graph connections by modifying the connections dictionary.
Specify the starting and goal nodes in the start_node and goal_node variables.
Run the program and it will print out the path from the starting node to the goal node, if it exists.
Sample Graph
Here is an example graph to show the format for the connections dictionary.

connections = {}
connections["Royian"] = {"George", "Frank","Adam"}
connections["George"] = {"Royian"}
connections["Frank"] = {"Royian"}
connections["Adam"] = {"Royian", "Ema", "Bob"}
connections["Ema"] = {"Bob", "Dolly","Adam"}
connections["Bob"] = {"Ema", "Adam","Dolly"}
connections["Dolly"] = {"Bob","Ema"}

This graph has nodes Royian, George, Frank, Adam, Ema, Bob, and Dolly with connections between them as described above.

Output
The program will output the path from the starting node to the goal node if it exists, and the tree traversed to find it. If no path exists, the program will output an appropriate message.



ucs_ex2

Uniform Cost Search Algorithm
This code implements the uniform cost search algorithm to find the shortest path between two points on a map, given the locations and connections between the points.

Usage
Modify the connections and location variables to define the map.
Call the uniform_cost_search(start, goal, connections, location) function, passing in the starting and goal points, as well as the connections and location variables.
The function returns the shortest path, the distance, the number of levels, the number of nodes expanded, and the search tree.
Example
start = "Bus Stop"
goal = "Canteen"
path, distance, level, num_expanded, tree = uniform_cost_search(start, goal, connections, location)
print("Path:", path)
print("Distance:", distance)
print("Number of levels:", level)
print("Number of nodes expanded:", num_expanded)
print("Tree:", tree)

This will output the shortest path, the distance, the number of levels, the number of nodes expanded, and the search tree for the given start and goal points.



