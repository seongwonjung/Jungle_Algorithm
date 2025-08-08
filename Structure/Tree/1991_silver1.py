import sys
input = sys.stdin.readline
N = int(input())
tree = {}
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = (left, right)

def preorder(node):
    if node == '.':
        return ""
    left, right = tree[node]
    return node + preorder(left) + preorder(right)

def inorder(node):
    if node == '.':
        return ""
    left, right = tree[node]
    return inorder(left) + node + inorder(right)

def postorder(node):
    if node == '.':
        return ""
    left, right = tree[node]
    return postorder(left) + postorder(right) + node

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))

# import sys
# input = sys.stdin.readline
# tree = {}
# n = int(input())
# for _ in range(n):
#     parent, left, right = input().split()
#     tree[parent] = (left, right)

# def preorder(node):
#     if node == '.':
#         return ""
#     left, right = tree[node]
#     return node + preorder(left) + preorder(right)

# def inorder(node):
#     if node == '.':
#         return ""
#     left, right = tree[node]
#     return inorder(left) + node + inorder(right)

# def postorder(node):
#     if node == '.':
#         return ""
#     left, right = tree[node]
#     return postorder(left) + postorder(right) + node
# print(preorder('A'))
# print(inorder('A'))
# print(postorder('A'))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# def preorder(node):
#     if node == None:
#         return ""
#     return node.data + preorder(node.left) + preorder(node.right)

# def inorder(node):
#     if node == None:
#         return ""
#     return inorder(node.left) + node.data + inorder(node.right)
    
# def postorder(node):
#     if node == None:
#         return ""
#     return postorder(node.left) + postorder(node.right) + node.data


# nodes = {}
# n = int(input())
# for _ in range(n):
#     parent, left, right = input().split()
#     if parent not in nodes:
#         nodes[parent] = Node(parent)
#     if left != '.':
#         if left not in nodes:
#             nodes[left] = Node(left)
#         nodes[parent].left = nodes[left]
#     if right != '.':
#         if right not in nodes:
#             nodes[right] = Node(right)
#         nodes[parent].right = nodes[right]

# # 시작점은 'A' 로 고정
# root = nodes['A']
# print(preorder(root))
# print(inorder(root))
# print(postorder(root))