import sys, heapq
from collections import deque
N, K = map(int ,input().split())
area = [list(map(int, input().split()))for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []
for y in range(N):
    for x in range(N):
        if area[y][x] != 0:
            heapq.heappush(virus, [area[y][x], x, y])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(q):
    v, x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and area[ny][nx] == 0:
            area[ny][nx] = v
            q.append([v, nx, ny])
                
q = deque()
l = len(virus)
for _ in range(l):
    q.append(heapq.heappop(virus))

for _ in range(S):
    l = len(q)
    for _ in range(l):
        bfs(q)

print(area[X-1][Y-1])