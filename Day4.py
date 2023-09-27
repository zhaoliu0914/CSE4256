from collections import deque

q = deque()
q.append(5)
q.append(6)
q.append(10)

print(q)

q.popleft()
print(q)


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


di = {0: [1, 3],
      1: [0, 4],
      2: [4],
      3: [0],
      4: [1, 2]}

result = bfs(di, 0)
