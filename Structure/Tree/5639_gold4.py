# import sys
# sys.setrecursionlimit(10**6)
# lines = sys.stdin.read().split()
# preorder = []
# for line in lines:
#     preorder.append(int(line))

# def solve(s, e):
#     if s >= e:
#         return
#     root = preorder[s]
#     mid = s + 1
#     while(mid < e and preorder[mid] < root):
#         mid += 1
    
#     solve(s+1, mid)     # 왼쪽 서브트리
#     solve(mid, e)       # 오른쪽 서브트리
#     print(root)       

# solve(0, len(preorder))

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
    
# class BST:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, key):
#         new = Node(key)
#         if self.root is None:
#             self.root = new
#             return

#         node = self.root
#         while True:
#             if key < node.key:
#                 if node.left is None:
#                     node.left = new
#                     return
#                 node = node.left
#             else:
#                 if node.right is None:
#                     node.right = new
#                     return
#                 node = node.right
    
#     def postorder(self):
#         result = []
#         self._postorder(self.root, result)
#         return result
    
#     def _postorder(self, node, result):
#         if node:
#             self._postorder(node.left, result)
#             self._postorder(node.right, result)
#             result.append(node.key)
            
# bst = BST()
# lines = sys.stdin.read().split()
# for line in lines:
#     bst.insert(int(line))

# for i in bst.postorder():
#     print(i)
