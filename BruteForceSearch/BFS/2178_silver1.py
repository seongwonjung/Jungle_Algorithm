import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().strip().split())
board = [list(map(int, input().strip()))for _ in range(n)]
# (0,0) 에서 시작 -> (n-1, m-1) 까지의 최단거리를 구해라
dx = [1,-1, 0, 0]
dy = [0, 0, -1, 1]
vst = [[False]*m for _ in range(n)]
def bfs(x, y):
    q = deque()
    vst[y][x] = True
    q.append([x, y, 1])
    while(q):
        x, y, dist = q.popleft()
        if y == n-1 and x == m-1:
            return dist
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or vst[ny][nx] or board[ny][nx] == 0:
                continue
            q.append([nx, ny, dist+1])
            vst[ny][nx] = True
    return -1
rst = bfs(0,0)
print(rst)