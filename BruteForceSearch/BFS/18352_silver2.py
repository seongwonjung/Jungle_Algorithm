import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
edge = [[] for _ in range(n+1)]
dist = [-1]*(n+1)
for _ in range(1, m+1):
    a, b = map(int, input().split())
    edge[a].append(b)

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    
    while q:
        x = q.popleft()
        for y in edge[x]:
            if dist[y] == -1:
                dist[y] = dist[x]+1
                q.append(y)
bfs(x)
rst = [i for i in range(1, n+1) if dist[i] == k]
if not rst:    print(-1)
else:
    for i in sorted(rst):
        print(i)




# dijkstra 풀이
# import sys, heapq, math
# input = sys.stdin.readline
# n, m, k, x = map(int, input().split())
# INF = math.inf
# edge = [[] for _ in range(n+1)]
# dist = [INF]*(n+1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     edge[a].append([1, b])

# heap = [[0, x]]
# dist[x] = 0
# while(heap):
#     ew, ev = heapq.heappop(heap)
#     if dist[ev] != ew:
#         continue
#     for nw, nv in edge[ev]:
#         if dist[nv] > ew + nw:
#             dist[nv] = ew + nw
#             heapq.heappush(heap, [dist[nv], nv])

# rst = []
# for i in range(1, n+1):
#     if dist[i] == k:
#         rst.append(i)
# if not rst:    print(-1)
# else:
#     for i in rst:
#         print(i)