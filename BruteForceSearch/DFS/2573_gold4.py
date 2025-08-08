# 아이디어
# 처음에 빙산이 있는 곳을 리스트에 담는다
# 빙산 마다 둘러쌓여 있는 만큼 - 시킨다. (0이하가 되면 리스트에서 빼버림)
# dfs 로 몇 덩이 인지 센다. 2 보다 커지면 종료
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]
iceberg = []
for y in range(n):
    for x in range(m):
        if board[y][x] != 0:
            iceberg.append([y, x, board[y][x]])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def cnt_around(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 0:
            cnt += 1
    return cnt

def dfs(x, y, vst):
    vst[y][x] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not vst[ny][nx] and board[ny][nx] != 0:
                dfs(nx, ny,vst)

time = -1
while iceberg:
    time += 1
    vst = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(len(iceberg)):
        y, x, h = iceberg[i]
        if not vst[y][x]:
            dfs(x,y,vst)
            cnt+=1
    
    if cnt >= 2:
        print(time)
        sys.exit()
        
    deltas = []
    for i in range(len(iceberg)):
        y, x, h = iceberg[i]
        deltas.append(h - cnt_around(x, y))
    
    new_iceberg = []
    for i in range(len(iceberg)):
        y, x, h = iceberg[i]
        if deltas[i] > 0:
            board[y][x] = deltas[i]
            new_iceberg.append([y,x,deltas[i]])
        else:
            board[y][x] = 0
    iceberg = new_iceberg
        

# 녹아 없어질때까지 2덩이가 안될 경우
print(0)