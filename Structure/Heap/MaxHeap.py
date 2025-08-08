class MaxHeap():

    def __init__(self):
        self.data = []
    
    # 부모 노드 = (idx-1) // 2
    def _parent(self, idx):
        return (idx - 1)//2
    
    # 왼쪽 자식 노드 = idx * 2 + 1
    def _left(self, idx):
        return idx*2 + 1
    
    # 오른쪽 자식 노드 = idx * 2 + 2
    def _right(self, idx):
        return idx*2 + 2
    
    # swap
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    def push(self, x):
        self.data.append(x)
        self.shift_up(len(self.data)-1)
    
    def pop(self):
        n = len(self.data)
        if n == 0:
            return 0
        self._swap(0, n-1)
        max_val = self.data.pop()
        if self.data:
            self.shift_down(0)
        return max_val
    
    def shift_down(self, idx):
        n = len(self.data)
        while True:
            l, r = self._left(idx), self._right(idx)
            largest = idx
            if l < n and self.data[l] > self.data[largest]:
                largest = l
            if r < n and self.data[r] > self.data[largest]:
                largest = r
            if largest == idx:
                break
            self._swap(largest, idx)
            idx = largest
    
    def shift_up(self, idx):
        while idx > 0:
            p = self._parent(idx)   # idx 의 부모 인덱스
            if self.data[p] >= self.data[idx]:
                break
            self._swap(p, idx)
            idx = p