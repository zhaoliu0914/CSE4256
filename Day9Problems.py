class Node:
    def __init__(self, value, left_child = None, right_child = None):
        self.value = value
        self.left = left_child
        self.right = right_child

    def __str__(self):
        return str(self.value)

# Problem 1
def is_full(root):
    fulled = True
    if root is not None:
        if (root.left is None and root.right is None) or (root.left is not None and root.right is not None):
            fulled = is_full(root.left)
            if fulled is True:
                fulled = is_full(root.right)
        else:
            fulled = False
    return fulled

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4)
n6 = Node(6, n7)
n3 = Node(3, None, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = is_full(n1)
print("is full ", result)

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4)
n6 = Node(6)
n3 = Node(3, n8, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = is_full(n1)
print("is full ", result)


# Problem 2
def height(root):
    h = 0
    if root is not None:
        left_height = height(root.left) + 1
        right_height = height(root.right) + 1
        h = left_height
        if right_height > left_height:
            h = right_height
    return h

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4)
n6 = Node(6)
n3 = Node(3, n8, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = height(n1)
print("height: ", result)

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4, n7, None)
n6 = Node(6)
n3 = Node(3, n8, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = height(n1)
print("height: ", result)


# Problem 3
def num_nodes(root):
    num = 0
    if root is not None:
        leftNum = num_nodes(root.left)
        rightNum = num_nodes(root.right)
        num = leftNum + rightNum + 1
    return num

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4, n7, None)
n6 = Node(6)
n3 = Node(3, None, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = num_nodes(n1)
print("number of nodes: ", result)

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4, n7, None)
n6 = Node(6)
n3 = Node(3, n8, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = num_nodes(n1)
print("number of nodes: ", result)


# Problem 4
def is_perfect(root):
    perfect = True
    

    return perfect

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4, n7, None)
n6 = Node(6)
n3 = Node(3, None, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = is_perfect(n1)
print("is perfect: ", result)

n8 = Node(8)
n5 = Node(5)
#n7 = Node(7)
n4 = Node(4)
n6 = Node(6)
n3 = Node(3, n8, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = is_perfect(n1)
print("is perfect: ", result)


# Problem 5
def is_degenerate(root):
    degenerate = True
    if root is not None:
        if root.left is None and root.right is None:
            degenerate = True
        elif root.left is not None and root.right is not None:
            degenerate = False
        else:
            degenerate = True

    return degenerate

n8 = Node(8)
n5 = Node(5)
n7 = Node(7)
n4 = Node(4, n7, None)
n6 = Node(6)
n3 = Node(3, None, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

result = is_degenerate(n1)
print("is degenerate: ", result)

n8 = Node(8)
n5 = Node(5)
#n7 = Node(7)
n4 = Node(4)
n6 = Node(6, n5, None)
n3 = Node(3, n8, None)
n2 = Node(2, None, n6)
n1 = Node(1, n2, None)

result = is_degenerate(n1)
print("is degenerate: ", result)


# Problem 6
def search_bst(root, num):
    isFound = False
    if root is not None:
        currentValue = root.value
        if num == currentValue:
            isFound = True
        elif num < currentValue:
            isFound = search_bst(root.left, num)
        else:
            isFound = search_bst(root.right, num)

    return isFound

n8 = Node(8)
n13 = Node(13)
n10 = Node(10)
n15 = Node(15, n13, None)
n3 = Node(3)
n2 = Node(2, None, n3)
n12 = Node(12, n10, n15)
n4 = Node(4, n2, n7)
root = Node(8, n4, n12)

result = search_bst(root, 7)
print("is number is binary search tree:", result)

n8 = Node(8)
n13 = Node(13)
n10 = Node(10)
n15 = Node(15, n13, None)
n3 = Node(3)
n2 = Node(2, None, n3)
n12 = Node(12, n10, n15)
n4 = Node(4, n2, n7)
root = Node(8, n4, n12)

result = search_bst(root, 14)
print("is number is binary search tree:", result)


#Problem 7
def insert_bst(root, num):
    if root is not None:
        currentValue = root.value
        if num < currentValue:
            if root.left is not None:
                search_bst(root.left, num)
            else:
                root.left = Node(num)
        else:
            if root.right is not None:
                search_bst(root.right, num)
            else:
                root.right = Node(num)


# Problem 8
def inOrder(node, indent):
    if node is not None:
        inOrder(node.left, indent + 1)

        for temp in range(indent * 4):
            print(" ", end='')
        print(node.value)

        inOrder(node.right, indent + 1)

n13 = Node(13)
n10 = Node(10)
n15 = Node(15, n13, None)
n3 = Node(3)
n2 = Node(2, None, n3)
n12 = Node(12, n10, n15)
n4 = Node(4, n2, n7)
root = Node(8, n4, n12)
inOrder(root, 0)


#Problem 7
def insert_bst(root, num):
    if root is not None:
        currentValue = root.value

        if num < currentValue:
            if root.left is not None:
                insert_bst(root.left, num)
            else:
                root.left = Node(num)
        else:
            if root.right is not None:
                insert_bst(root.right, num)
            else:
                root.right = Node(num)

print("before insert 5")
n13 = Node(13)
n10 = Node(10)
n15 = Node(15, n13, None)
n3 = Node(3)
n2 = Node(2, None, n3)
n12 = Node(12, n10, n15)
n4 = Node(4, n2, n7)
root = Node(8, n4, n12)
inOrder(root, 0)

print("after insert 5")
insert_bst(root, 5)
inOrder(root, 0)