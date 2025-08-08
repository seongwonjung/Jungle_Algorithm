class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return ""
    return node.key + preorder(node.left) + preorder(node.right)

def inorder(node):
    if node is None:
        return ""
    return inorder(node.left) + node.key + inorder(node.right)

def postorder(node):
    if node is None:
        return ""
    return postorder(node.left) + postorder(node.right) + node.key

n = int(input())
nodes = {}
for _ in range(n):
    parent, left, right = input().split()
    if parent not in nodes:
        nodes[parent] = Node(parent)
    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        nodes[parent].left = nodes[left]
    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        nodes[parent].right = nodes[right]

root = nodes['A']

print(preorder(root))
print(inorder(root))
print(postorder(root))