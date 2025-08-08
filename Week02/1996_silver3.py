import sys, heapq
from collections import deque

input = sys.stdin.readline
t = int(input().strip())

def get_order(docs, idx):
    q = deque()
    h = []
    for i in range(len(docs)):
        q.append(i)
        heapq.heappush(h, -docs[i])
    
    order = []
    
    while(q):
        if -h[0] > docs[q[0]]:
            q.append(q.popleft())
        else:
            i = q.popleft()
            heapq.heappop(h)
            order.append(i)
    return order.index(idx)+1

for _ in range(t):
    n , m = map(int, input().strip().split())
    docs = tuple(map(int, input().strip().split()))
    print(get_order(docs, m))