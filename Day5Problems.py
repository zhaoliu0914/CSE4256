from collections import deque

# Question 1
# takes a dictionary representation of a simple directed graph as its argument
# and returns a dictionary representation of its underlying simple graph.
# The underlying simple graph of a directed graph G is G with undirected edges.
def simple_d(di):
    undirected_graph = {}

    for k, v in di.items():
        vertex = []

        for temp in range(len(v)):
            vertex.append(v[temp])

        for tempK, tempV in di.items():
            if k in tempV and tempK not in vertex:
                vertex.append(tempK)

        undirected_graph[k] = vertex

    return undirected_graph


di = {0: [1, 2],
      1: [0],
      2: [4],
      3: [1, 2],
      4: [3]}

result = simple_d(di)
print(result)


# Question 2
# Write a function called simple m(mat) that takes a matrix representation of a simple directed graph
# as its argument and returns a matrix representation of its underlying simple graph.
def simple_m(mat):
    undirected_mat = []
    for i in range(len(mat)):
        undirected_mat.append([0] * len(mat[i]))

    for row in range(len(mat)):
        for column in range(len(mat[row])):
            if mat[row][column] == 1:
                undirected_mat[row][column] = 1
                undirected_mat[column][row] = 1

    return undirected_mat


mat = [[0, 1, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 1, 0]]

result = simple_m(mat)
print(result)


# Question 3
# The transpose of a directed graph g is a graph with the edges of g reversed.
def transpose_dir_graph(di):
    transpose_di = {}

    for k, v in di.items():
        tempArray = []
        transpose_di[k] = tempArray

    for k, v in di.items():
        for item in v:
            transpose_di[item].append(k)

    return transpose_di


di = {0: [1, 2],
      1: [0],
      2: [4],
      3: [1, 2],
      4: [3]}

result = transpose_dir_graph(di)
print(result)


# Question 4
# Write a function called transpose m(mat) that takes a matrix representation of a directed graph
# and returns a matrix representation of its transpose.
def transpose_m(mat):
    transpose_mat = []

    for i in range(len(mat)):
        transpose_mat.append([0] * len(mat[i]))

    for row in range(len(mat)):
        for column in range(len(mat[row])):
            if mat[row][column] == 1:
                transpose_mat[column][row] = 1

    return transpose_mat


mat = [[0, 1, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 1, 0]]

result = transpose_m(mat)
print(result)


# Question 5
# Write a function called is connected(di) that takes a dictionary representing a simple graph
# as an argument and returns True if di is connected, False oth- erwise.

def is_connected(di):
    result = bfs(di, 0)
    if None in result:
        return False

    return True


# Implement Breadth-First Search (BFS)
def bfs(di, starting_node):
    # create an empty q
    q = deque()
    q.append(starting_node)
    # create a list to store the distances of nodes to starting_node
    # set the distances for all nodes to None.
    distances = [None] * len(di)
    # set the distance of the starting node to 0.
    distances[starting_node] = 0
    # while the queue is not empty
    while q:
        # pop off the node at the front of the queue
        current_node = q.popleft()
        # for every node adjacent to the current node
        for node in di[current_node]:
            # if the node hasn’t been visited yet
            if distances[node] == None:
                # set the distance of the node
                distances[node] = distances[current_node] + 1
                # add the node to the end of the queue
                q.append(node)
    return distances

d = {0 : [1, 3],
     1 : [0, 4],
     2 : [4],
     3 : [0],
     4 : [1, 2]}

result = bfs(d, 0)
print(result)

# Implement Breadth-First Search (BFS) takes a matrix as an argument, rather than a dictionary.
def bfs_m(mat, starting_node):
    q = deque()
    q.append(starting_node)
    distances = [None] * len(mat)
    distances[starting_node] = 0
    while q:
        current_node = q.popleft()
        for i in range(len(mat[current_node])):
            if mat[current_node][i] == 1 and distances[i] == None:
                distances[i] = distances[current_node] + 1
                q.append(i)
    return distances

