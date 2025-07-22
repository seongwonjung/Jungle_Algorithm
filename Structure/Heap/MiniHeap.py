class MiniHeap:
    def __init__(self):
        self.data = []
    
    # ----- 내부 유틸들 -----
    
    # 주의 - 시작 노드가 1이 아닌 0으로 시작함
    
    # 부모 노드 = (idx-1) // 2
    def _parent(self, idx):
        return (idx - 1)//2
    
    # 왼쪽 자식 노드 = idx * 2 + 1
    def _left(self, idx):
        return idx*2 + 1
    
    # 오른쪽 자식 노드 = idx * 2 + 2
    def _right(self, idx):
        return idx*2 + 2
    
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    # 삽입 O(long n)
    def push(self, item):
        self.data.append(item)
        self._sift_up(len(self.data) - 1)
    
    # 삭제 O(log n)
    def pop(self):
        if not self.data:
            raise IndexError("pop from empty heap")
        self._swap(0, -1)
        min_val = self.data.pop()
        self._sift_down(0)
        return min_val
    
    def peek(self):
        return self.data[0]
    
    # 노드를 append()로 추가 -> 맨 끝 인덱스에 추가됨
    # 최소힙에서 - 부모노드가 자신보다 작아야 한다는 성질을 맞추기 위해
    # 부모노드와 비교하며 swap
    def _sift_up(self, idx):
        while idx > 0:
            p = self._parent(idx)
            if self.data[p] <= self.data[idx]:  # 부모 노드가 더 작다면 종료
                break
            self._swap(p, idx)
            idx = p
    
    # 노드를 0, end 와 바꾼후 pop()으로 삭제 -> 0번째 노드와 스왑하므로 최소힙 성질에 맞지 않음
    # 부모노드(현재 idx)와 자식노드들과 비교해 가며 바꿔준다
    def _sift_down(self, idx):
        n = len(self.data)
        while True:
            l, r = self._left(idx), self._right(idx)
            smallest = idx
            if l < n and self.data[l] < self.data[smallest]:    
                smallest = l
            if r < n and self.data[r] < self.data[smallest]:
                smallest = r
            if smallest == idx:     # 부모 노드가 두 자식보다 작거나 같으면(=힙 조건 만족) 종료
                break
            # 왼쪽 자식노드와 오른쪽 자식 노드 중 더 작은 값이 smallest 에 담김
            # 더 작은 자식 노드와 idx swap
            self._swap(idx, smallest)
            # 바꾼 자식 노드의 인덱스를 가지고 위 과정 반복
            idx = smallest

# 사용 예
h = MiniHeap()
for v in [5, 2, 8, 1]:
    h.push(v)
    
while True:
    try:
        print(f"{h.pop()} ", end='')
    except IndexError:
        break