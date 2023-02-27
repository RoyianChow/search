from queue import Queue

# Define the graph
connections = {}
connections["Royian"] = {"George", "Frank","Adam"}
connections["George"] = {"Royian"}
connections["Frank"] = {"Royian"}
connections["Adam"] = {"Royian", "Ema", "Bob"}
connections["Ema"] = {"Bob", "Dolly","Adam"}
connections["Bob"] = {"Ema", "Adam","Dolly"}
connections["Dolly"] = {"Bob","Ema"}

def bfs(graph, start, goal):
    visited = set()  # keep track of visited nodes
    queue = Queue()  # create a queue for BFS
    queue.put(start)  # add the starting node to the queue
    parent = {start: None}  # keep track of the parent of each node
    
    while not queue.empty():
        node = queue.get()  # get the next node from the queue
        if node == goal:
            # construct the path from start to goal
            path = [node]
            while parent[node] is not None:
                path.append(parent[node])
                node = parent[node]
            path.reverse()
            return path
        if node not in visited:
            visited.add(node)  # mark the node as visited
            neighbors = graph.get(node, set())  # get the neighbors of the node
            for neighbor in neighbors:
                if neighbor not in visited:
                    parent[neighbor] = node  # set the parent of the neighbor
                    queue.put(neighbor)  # add the neighbor to the queue
    return None  # goal node not found

# Call the BFS function on the graph with starting node "Royian" and goal node "Dolly"
start_node = "Royian"
goal_node = "yasir"
if start_node not in connections:
    print(f"Error: start node {start_node} does not exist in the graph.")
elif goal_node not in connections:
    print(f"Error: goal node {goal_node} does not exist in the graph.")
else:
    path = bfs(connections, start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
        print(f"Tree traversed: {path[0]}", end='')
        for node in path[1:]:
            print(f" -> {node}", end='')
        print()
    else:
        print("Sorry, a relationship between the start and goal nodes could not be established.")
