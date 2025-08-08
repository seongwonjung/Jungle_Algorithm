# BFS 를 이용한 풀이
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = set()
    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.add((x, y))
    rst = 0
    while cabbages:
        q = deque()
        q.append((cabbages.pop()))
        rst += 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if (nx, ny) in cabbages:
                    q.append((nx, ny))
                    cabbages.remove((nx, ny))
    print(rst)
                
# DFS 를 이용한 풀이
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# T = int(input())
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def dfs(x,y):
#     vst[y][x] = True
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if 0 <= nx < M and 0 <= ny < N and ground[ny][nx] == 1 and not vst[ny][nx]:
#             dfs(nx, ny)

# for _ in range(T):
#     M, N, K = map(int, input().split())
#     ground = [[0]*M for _ in range(N)]
#     vst = [[False]*M for _ in range(N)]
#     cabbage = []
#     for _ in range(K):
#         x, y = map(int, input().split())
#         ground[y][x] = 1
#         cabbage.append([x,y])
#     rst = 0
#     for x, y in cabbage:
#         if not vst[y][x]:
#             dfs(x,y)
#             rst+=1
#     print(rst)