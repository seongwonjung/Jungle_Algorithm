import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dx = [1,1,2,2,-1,-1,-2,-2]
dy = [2,-2,1,-1,2,-2,1,-1]
for _ in range(T):
    L = int(input())
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    # 이동할 수 있는 방향은 8방향 vst 처리
    vst = [[False]*L for _ in range(L)]
    q = deque()
    q.append([s_x, s_y, 0])
    vst[s_y][s_x] = True
    while q:
        x, y, c = q.popleft()
        if x == e_x and y == e_y:
            print(c)
            break
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < L and 0 <= ny < L and not vst[ny][nx]:
                vst[ny][nx] = True
                q.append([nx,ny,c+1])