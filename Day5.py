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

    # create a list to store the distance of nodes to starting_node
    # set the distance for all nodes to None
    distance = [None] * len(di)

    # set the distance of the starting_node to 0
    distance[starting_node] = 0

    # while the queue is not empty
    while q:
        # pop off the node at the front of the queue
        current_node = q.popleft()

        # for every node adjacent to current_node
        for node in di[current_node]:
            # if the code hasnot been visited yey.
            if distance[node] == None:
                # set the distance of the node
                distance[node] = distance[current_node] + 1

                # add the node to the end of the queue
                q.append(node)

    return distance


di = {0: [1, 3],
      1: [0, 4],
      2: [4],
      3: [0],
      4: [1, 2]}

distance = bfs(di, 0)

print(distance)
