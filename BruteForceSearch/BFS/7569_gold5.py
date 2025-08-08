import sys
from collections import deque
input = sys.stdin.readline
# 가로, 세로, 높이
M, N, H = map(int, input().split())
# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 없음
# box[z][y][x] 형태 3차원 배열
box = [
    [list(map(int, input().split())) for _ in range(N)]
    for _ in range(H)
]

if not any(0 in layer_row for layer in box for layer_row in layer):
    print(0)
    sys.exit()

dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
days = [[[-1]*M for _ in range(N)] for _ in range(H)]
q = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                q.append((z,y,x))
for z,y,x in q:
    days[z][y][x] = 0

while q:
    z, y, x = q.popleft()
    for dz_i, dy_i, dx_i in zip(dz, dy, dx):
        nz, ny, nx = z+dz_i, y+dy_i, x+dx_i
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if box[nz][ny][nx] == 0 and days[nz][ny][nx] == -1:
                box[nz][ny][nx] = 1
                days[nz][ny][nx] = days[z][y][x] + 1
                q.append((nz, ny, nx))
                
# 1) 익지 못한 토마토가 있는지 검사
if any(
    box[z][y][x] == 0 and days[z][y][x] == -1
    for z in range(H)
    for y in range(N)
    for x in range(M)
):
    print(-1)
    sys.exit()

# 2) 모두 익었으면 최대 일수 출력
ans = max(
    days[z][y][x]
    for z in range(H)
    for y in range(N)
    for x in range(M)
    if box[z][y][x] != -1
)
print(ans)