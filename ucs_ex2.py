import heapq

connections = {}
connections["Bus Stop"] = {"Library"}
connections["Library"] = {"Bus Stop", "Car Park", "Student Center"}
connections["Car Park"] = {"Library", "Maths Building", "Store"}
connections["Maths Building"] = {"Car Park", "Canteen"}
connections["Student Center"] = {"Library", "Store" , "Theater"}
connections["Store"] = {"Student Center", "Car Park", "Canteen", "Sports Center"}
connections["Canteen"] = {"Maths Building", "Store", "AI Lab"}
connections["AI Lab"] = {"Canteen"}
connections["Theater"] = {"Student Center", "Sports Center"}
connections["Sports Center"] = {"Theater", "Store"}

#location of all the places
location = {}
location["Bus Stop"] = [2, 8]
location["Library"] = [4, 8]
location["Car Park"] = [1, 4]
location["Maths Building"] = [4, 1]
location["Student Center"] = [6, 8]
location["Store"] = [6, 4]
location["Canteen"] = [6, 1]
location["AI Lab"] = [6, 0]
location["Theater"] = [7, 7]
location["Sports Center"] = [7, 5]



def uniform_cost_search(start, goal, connections, location):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()
    level = 0
    num_expanded = 0
    tree = {}
    
    while frontier:
        (cost, current, path) = heapq.heappop(frontier)
        if current == goal:
            return path, cost, level, num_expanded, tree
        if current in explored:
            continue
        explored.add(current)
        num_expanded += 1
        if level == 0:
            tree[current] = {}
        for neighbor in connections[current]:
            new_cost = cost + distance(location[current], location[neighbor])
            new_path = path + [neighbor]
            heapq.heappush(frontier, (new_cost, neighbor, new_path))
            if neighbor not in tree:
                tree[neighbor] = {}
            tree[current][neighbor] = new_cost
        level += 1
    
    return "No path found", None, None, num_expanded, tree

def distance(location1, location2):
    return ((location1[0]-location2[0])**2 + (location1[1]-location2[1])**2) ** 0.5

# Example usage:

start = "Bus Stop"
goal = "Canteen"
path, distance, level, num_expanded, tree = uniform_cost_search(start, goal, connections, location)
print("Path:", path)
print("Distance:", distance)
print("Number of levels:", level)
print("Number of nodes expanded:", num_expanded)
print("Tree:", tree)
