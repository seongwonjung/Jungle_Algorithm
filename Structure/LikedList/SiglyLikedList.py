class Node:
    def __init__(self, data, next_ = None):
        self.data = data    # 노드가 저장할 데이터
        self.next = next_    # 다음 노드를 가리키는 포인터
        
class SinglyLinkedList:
    def __init__(self, iterable = None):
        self.head = None    # 리스트의 시작을 가리키는 포인터
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)
    
    def append(self, data):
        new = Node(data)
        if not self.head:       # 빈 리스트라면
            self.head = new
        else:
            cur = self.head
            while cur.next:     # 끝까지 순회
                cur = cur.next
            cur.next = new
        self.size += 1
        
    def prepend(self, data):    # 맨 앞에 삽입
        self.head = Node(data, self.head)
        self.size += 1
    
    def insert(self, index: int, data):
        if index <= 0:
            return self.prepend(data)
        if index >= self.size:
            return self.append(data)
        
        prev = self._node_at(index-1)
        prev.next = Node(data, prev.next)
        self.size += 1
        
    def pop(self, index: int = -1):
        # index 위치 노드 제거 후 데이터 반환
        if self.size == 0:
            raise IndexError("pop from empty list")
        if index < 0:
            index += self.size
        if not (0 <= index < self.size):
            raise IndexError("pop index out of range")
        
        if index == 0:
            removed = self.head
            self.head = self.head.next
        else:
            prev = self._node_at(index-1)
            removed = prev.next
            prev.next = removed.next
        self.size -= 1
        return removed.data
    
    def remove(self, value):
        cur = self.head
        prev = None
        while cur:
            if cur.data == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        return False
    
    def find(self, value):
        idx, cur = 0, self.head
        while cur:
            if cur.data == value:
                return idx
            cur, idx = cur.next, idx + 1
        return -1
        
    
    def _node_at(self, index):
        # index 번째 노드 객체 반환
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur
    
    def __len__ (self):
        return self.size
    
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next
            
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        self.head = prev
    
    def __repr__(self):
        return "SinglyLinkedList([" + ", ".join(map(str, self)) + "])"
            

lst = SinglyLinkedList([10, 20, 30])
lst.append(40)            # → 10 → 20 → 30 → 40
lst.prepend(5)            # 5 → ...
lst.insert(2, 15)         # 5 → 10 → 15 → 20 → 30 → 40
print("원본:", lst)

lst.pop()                 # 맨 뒤 40 제거
lst.remove(15)            # 값 15 제거
print("삭제 후:", lst)    # 5 → 10 → 20 → 30

print("20 위치:", lst.find(20))   # 2
lst.reverse()
print("역순:", lst)       # 30 → 20 → 10 → 5


# - 내가 이해한 내용 적어보기
#     - 연결리스트(linked list)는 노드로 이루어져 있다. node는 값을 담는 data와 다음노드를 가리키는 next로 이루어져 있다.
#     - 배열같이 물리적인 주고 공간이 순차적이지 않다. node의 next로 연결된 논리적인 선형 자료구조임.
#     - 가장 중요한 삽입, 삭제는 tail 이 있다는 가정 하에 맨 앞(head), 맨 뒤(tail)인 경우 시간 복잡도 O(1)이다. 중간에 삽입, 삭제 할 경우 해당 노드를 찾는 과정이 추가 되기 때문에 O(n)의 시간 복잡도가 된다.
#     - 위에서 말한대로 연결리스트는 next 참조를 통한 순차적인 자료 구조 이기 때문에 특정 노드를 찾는 과정은 최대 O(n) 이 소요된다.( k번째 노드라면 O(k))
#     - 배열에서는 pop(0) 을 실행할 경우 0번째 인덱스의 값을 지우고 오른쪽에 있는 원소들을 왼쪽으로 밀어 넣는다. 따라서 시간복잡도 O(n)이 소요되는데 그냥 0번째 인덱스 공간 자체를 지우고 맨앞을 1번 인덱스를 가리키게 하는건 안될까? → 배열은 블럭단위로 할당되기 때문에 0~10 짜리 공간을 할당 받고 0번쨰 만 free() 하는것이 불가능하게 설계 되어있다. 따라서 방금 말했던 과정은 불가능 더 자세한 내용은 생략 → 전반적인 내용은 한공간을 자르는 과정이 불가능하게 되어있고, 가능하게 바꾼다면 관련된 capacity-size base 로 저장되기 때문에 다른 연산들(ex 삽입, 삭제)에 영향을 미쳐 관련된 내용들도 수정해줘야하기 때문에 비효율적이라고 한다.
#     - 파이썬에서는 deque를 이용해서 likedlist처럼 사용한다고 한다. list로도 가능하긴 한데 두 개의 차이점은 list는 일종의 동적배열이라고 생각하면 되고, deque는 원형 버퍼라고 생각해라
