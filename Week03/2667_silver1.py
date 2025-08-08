import sys
sys.setrecursionlimit(10**6)
N = int(input())
board = [list(map(int, input().strip()))for _ in range(N)]
vst = [[False]*(N)for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt = 0
def dfs(x, y):
    global cnt
    vst[y][x] = True
    for i in range(4):
        ny, nx = x+dx[i], y+dy[i],
        if 0 <= ny < N and 0 <= nx < N and not vst[ny][nx]:
            if board[ny][nx] == 1:
                cnt += 1
                dfs(nx, ny)

rst = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and not vst[y][x]:
            cnt = 1
            dfs(x,y)
            rst.append(cnt)

print(len(rst))
for i in sorted(rst):
    print(i)