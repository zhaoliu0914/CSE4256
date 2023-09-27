class Node:
    def __init__(self, value, left_child = None, right_child = None):
        self.val = value
        self.left = left_child
        self.right = right_child

    def __str__(self):
        return str(self.val)

n1 = Node(7)
print(n1)
print(n1.left)
print(n1.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n5
n2.right = n6
n6.left = n7
n3.right = n4


n5 = Node(5)
n7 = Node(7)
n4 = Node(4)
n6 = Node(6, n7)
n3 = Node(3, None, n4)
n2 = Node(2, n5, n6)
n1 = Node(1, n2, n3)

print(n1)
print(n1.left)
print(n1.right)

def preOrder(node, indent):
    if node is not None:
        for temp in range(indent * 4):
            print(" ", end='')
        print(node.val)

        preOrder(node.left, indent + 1)
        preOrder(node.right, indent + 1)

preOrder(n1, 0)
print("========================")

def inOrder(node, indent):
    if node is not None:
        preOrder(node.left, indent + 1)

        for temp in range(indent * 4):
            print(" ", end='')
        print(node.val)

        preOrder(node.right, indent + 1)

inOrder(n1, 0)