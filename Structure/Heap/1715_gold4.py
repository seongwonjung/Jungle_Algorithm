import sys
import heapq
input = sys.stdin.readline
n = int(input().strip())
if n == 1:         # 묶음이 하나면 비용 0
    print(0)
    sys.exit()
heap = [int(input().strip())for _ in range(n)]
heapq.heapify(heap)
cost = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    cost += a+b
    
print(cost)