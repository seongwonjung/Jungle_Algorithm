class TrieNode:
    def __init__(self):
        self.children = {}  # 자식 노드(문자: 노드)
        self.is_end = False # 단어 끝 여부
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root    # 루트에서 시작
        for char in word:   # 단어의 모든 문자 하나씩 순회
            if char not in node.children:   # 현재 노드에 이 문자가 없으면
                node.children[char] = TrieNode()    # 새 노드를 만들어 자식으로 추가
            node = node.children[char]  # 다음 글자 처리를 위해 아래(자식노드)로 이동
        node.is_end = True  # 마지막 글자에서 끝남
        
    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):
        return self._find_node(prefix) is not None
    
    def _find_node(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node