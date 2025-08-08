import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().strip()))for _ in range(N)]
# 0 -> 검은 방, 1 -> 흰 방
# 시작 (0,0) 도착 (N-1, N-1)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque()
dq.append((0,0,0))
vst = [[False]*N for _ in range(N)]
rst = 0
vst[0][0] = True
while dq:
    y, x, cost = dq.popleft()
    if y == N-1 and x == N-1:
        rst = cost
        break
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < N and 0 <= nx < N and not vst[ny][nx]:
            vst[ny][nx] = True
            if board[ny][nx] == 1:
                dq.appendleft((ny,nx, cost))
            else:
                dq.append((ny,nx, cost+1))
print(rst)

# 0-1 BFS 방식
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# board = [list(map(int, input().strip())) for _ in range(n)]
# INF = sys.maxsize
# dist = [[INF]*n for _ in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# def zero_one_bfs(x, y):
#     dq = deque()
#     dq.append([y, x])
#     dist[y][x] = 0
#     while dq:
#         y, x = dq.popleft()
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if 0 <= ny < n and 0 <= nx < n:
#                 next_cost = dist[y][x] + (1 if board[ny][nx] == 0 else 0)
#                 if dist[ny][nx] > next_cost:
#                     dist[ny][nx] = next_cost
#                     if board[ny][nx] == 0:
#                         dq.appendleft([ny, nx])
#                     else:
#                         dq.append([ny, nx])
#     return dist[n-1][n-1]
# print(zero_one_bfs(0,0))

# dijkstra 풀이방식
# import sys, heapq
# input = sys.stdin.readline
# n = int(input())
# INF = sys.maxsize
# board = [list(map(int, input().strip())) for _ in range(n)]
# dist = [[INF]*n for _ in range(n)]
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# # 벽 부순 횟수, y, x
# heap = [[0,0,0]]
# dist[0][0] = 0
# while heap:
#     cost, y, x = heapq.heappop(heap)
#     # 종료 (n-1, n-1) 도착하면 그때의 cost
#     if x == n-1 and y == n-1:
#         print(cost)
#         break
#     if dist[y][x] != cost:
#         continue
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             next_cost = cost+1 if board[ny][nx] == 0 else cost
#             if next_cost < dist[ny][nx]:
#                 dist[ny][nx] = next_cost
#                 heapq.heappush(heap, [next_cost, ny, nx])