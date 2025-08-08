# 노드 클래스: 트리의 각 노드를 표현
class Node:
    def __init__(self, data):
        self.data = data    # 노드 값
        self.left = None    # 왼쪽 자식 노드
        self.righht = None  # 오른쪽 자식 노드
        
# BST - Binary Search Tree 이진탐색트리
class BST:
    def __init__(self):
        self.root = None
    
    # 삽입 함수(puplic)
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)  # 루트가 없으면 새 노드를 루트로
        else:
            self._insert(self.root, data)   # 루트부터 재귀적으로 삽입
    
    # 삽입 함수(internal recursive)
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = node(data)
            else:
                self._insert(node.right, data)
        # 중복은 무시함
    
    # 탐색 함수(public)
    def search(self, data):
        return self._search(self.root, data)
    
    # 탐색 함수(internal recursive)
    def _search(self, node, data):
        if node is None:    # 리프 노드 까지 간 후 없으면 None -> 찾는 값이 없을 때 False
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search(node.left, data)    # 작으면 왼쪽 탐색
        else:
            return self._search(node.right, data)   # 크면 오른쪽 탐색
    
    # 중위 순회 (왼 -> 루트 -> 오)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.data)
            self._inorder(node.right, result)
    
    # 전위 순회 (루트 -> 왼 -> 오)
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)
    
    # 후위 순회 (왼 -> 오 -> 루트)
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)
    
    # 삭제 함수(public)
    def delete(self, data):
        self.root = self._delete(self.root, data)
    
    # 삭제 함수(internal recursive)
    def _delete(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self._delete(node.left, data)   # 왼쪽에서 찾기
        elif data > node.data:
            node.right = self._delete(node.right, data) # 오른쪽에서 찾기
        else:   # 찾음
            # Case 1: 리프 노드인 경우
            if node.left is None and node.right is None:
                return None
            # Case 2: 자식이 하나만 있는 경우
            if node.left is None:   # 왼쪽 자식이 없다? 그럼 오른쪽 자식 반환
                return node.right
            if node.right is None:  # 오른쪽 자식이 없다? 그럼 왼쪽 자식 반환
                return node.left
            # Case 3: 자식이 둘 다 있는 경우
            # 오른쪽 서브트리에서 최소값을 가져와 현재 노드에 대체
            min_node = self.get_min(node.right)
            node.data = min_node.data
            # 중복된 최소값을 삭제
            node.right = self.delete(node.right, min_node.data)
        return node
    
    # 현재 노드를 루트로 하는 서브트리의 최소값 찾기
    def get_min(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node
    
    # 특정 노드의 후계자 (inorder successor) 찾기
    def get_next(self, target_node):
        # Case 1: 오른쪽 자식이 있는 경우 -> 그 서브트리의 최소값
        if target_node.right:
            return self.get_min(target_node.right)
        # Case 2: 오른쪽이 없을 때 -> 조상 중 처음 왼쪽 자식이 되는 부모
        successor = None
        current = self.root
        while current:
            if target_node.data < current.data:
                successor = current
                current = current.left
            elif target_node.data > current.data:
                current = current.righht
            else:
                break
        return successor