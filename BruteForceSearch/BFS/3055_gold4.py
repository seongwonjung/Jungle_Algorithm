# import sys
# from collections import deque
# input = sys.stdin.readline
# R, C = map(int, input().split())
# board =[list(input().strip())for _ in range(R)]
# start_x, start_y = 0,0
# sq = deque()
# wq = deque()
# for r in range(R):
#     for c in range(C):
#         if board[r][c] == "S":  start_x, start_y = c, r
#         if board[r][c] == "*":  wq.append([r,c])

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# dist = [[-1]* C for _ in range(R)]
# dist[start_y][start_x] = 0
# sq.append([start_y, start_x])

# while sq:
#     # 물 먼저 채우기
#     for _ in range(len(wq)):
#         y, x = wq.popleft()
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i] 
#             if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == ".":
#                 board[ny][nx] = "*"
#                 wq.append([ny, nx])
#     # 고슴도치 이동
#     for _ in range(len(sq)):
#         y, x = sq.popleft()
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if 0 <= ny < R and 0 <= nx < C:
#                 if board[ny][nx] == "D":
#                     print(dist[y][x]+1)
#                     sys.exit()
#                 if board[ny][nx] == "." and dist[ny][nx] == -1:
#                     dist[ny][nx] = dist[y][x] + 1
#                     sq.append([ny, nx])
# print("KAKTUS")