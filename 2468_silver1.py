import sys
# 런타임 에러나와서 추가 -> 재귀 깊이 10^8까지로 늘림
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
vst = [[False]*n for _ in range(n)]
ground = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

# 처음에 map활용할 생각을 못했음
max_height = max(map(max, ground))

print(max_height)
# 비 내리면 전체 -1
# 0보다 작거나 같아지면 True로
def raining():
    global ground, vst, n
    vst = [[False]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            ground[y][x] -= 1
            if ground[y][x] <= 0:
                vst[y][x] = True
    return            

def dfs(x, y):
    global vst, dx, dy, n
    if vst[y][x]:
        return
    vst[y][x] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (0 <= nx < n and 0 <= ny < n and not vst[ny][nx]):
            dfs(nx, ny)
            
i = 0
rst = 1
while(i < max_height):
    raining()
    cnt = 0
    for y in range(n):
        for x in range(n):
            if not vst[y][x]:
                cnt += 1
                dfs(x,y)
    rst = max(rst, cnt)
    i += 1
print(rst)