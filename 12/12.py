with open("./12/12-input.txt", "r") as f:
    d = f.read().split("\n")

import math

# from queue import PriorityQueue

height_grid = [[] for _ in range(len(d))]
s = None
e = None

# pq = PriorityQueue()  # dist, (node_id, x_pos, y_pos)
nodes = {}
nodes_pos = {}
n = 0

# Parsing the basic input data, calculating heights, creating nodes etc.
for y, row in enumerate(d):
    for x, c in enumerate(row):
        # Setup nodes
        # pq.put(0 if c == "S" else math.inf, (n, x, y))  # S is dist 0 else infinity
        nodes[n] = {"pos": (x, y), "al": []}  # each node pos and al
        nodes_pos[(x, y)] = n
        n += 1
        # Calculate height grid
        if c.isupper():
            if c == "S":
                s = x, y
                height_grid[y].append(1)
            if c == "E":
                e = x, y
                height_grid[y].append(26)
        else:
            height_grid[y].append(ord(c) - 96)

# Start and End
# print(s, e)
mx_y = len(height_grid)
mx_x = len(height_grid[0])


# Now I'm going to calculate the graph with distance to each neighbour for the nodes
for node in nodes:
    pos, al = nodes[node].values()
    x, y = pos

    # Calculate distance base value
    nv = height_grid[y][x]

    # TODO: if target is not in the correct direction add penalty?
    # max 1 diff for 'path' to be available

    if y != 0:  # top value
        tv = height_grid[y - 1][x]
        if tv - nv <= 1:
            al.append((nodes_pos[(x, y - 1)], 1))  # + abs(nv - tv)))

    if y != mx_y - 1:  # bottom value
        bv = height_grid[y + 1][x]
        if bv - nv <= 1:
            al.append((nodes_pos[(x, y + 1)], 1))  # + abs(nv - bv)))

    if x != 0:  # left value
        lv = height_grid[y][x - 1]
        if lv - nv <= 1:
            al.append((nodes_pos[(x - 1, y)], 1))  # + abs(nv - lv)))

    if x != mx_x - 1:  # right value
        rv = height_grid[y][x + 1]
        if rv - nv <= 1:
            al.append((nodes_pos[(x + 1, y)], 1))  # + abs(nv - rv)))


def naive_dijkstras(graph, root):
    n = len(graph)
    # initialize distance list as all infinities
    dist = [math.inf for _ in range(n)]
    # set the distance for the root to be 0
    dist[root] = 0
    # initialize list of visited nodes
    visited = [False for _ in range(n)]
    # loop through all the nodes
    for _ in range(n):
        # "start" our node as -1 (so we don't have a start node yet)
        u = -1
        # loop through all the nodes to check for visitation status
        for i in range(n):
            # if the node 'i' hasn't been visited and
            # we haven't processed it or the distance we have for it is less
            # than the distance we have to the "start" node
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        # all the nodes have been visited or we can't reach this node
        if dist[u] == math.inf:
            break
        # set the node as visited
        visited[u] = True
        # compare the distance to each node from the "start" node
        # to the distance we currently have on file for it
        for v, l in graph[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist


graph = {k: nodes[k]["al"] for k in nodes}
root_node_id = nodes_pos[s]
end_node_id = nodes_pos[e]
res = naive_dijkstras(graph, root_node_id)
print("Part 1: ", res[end_node_id])

root_nodes = []
for k, v in nodes.items():
    pos = v["pos"]
    x, y = pos
    if height_grid[y][x] == 1:
        root_nodes.append(nodes_pos[pos])

lowest = []
for root_node_id in root_nodes:
    res = naive_dijkstras(graph, root_node_id)
    lowest.append(res[end_node_id])

print("Part 2: ", min(lowest))

# Create an index of nodes that's an int, that points to pos in grid, and
# Generate distance grid
