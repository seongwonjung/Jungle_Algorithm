import sys
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(input().strip())for _ in range(N)]
vst = [[False]*(M)for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(M):
        if not vst[y][x]:
            if board[y][x] == '-':
                ans += 1
                while 0 <= y < N and 0<= x < M and board[y][x] == '-':
                    vst[y][x] = True
                    x += 1
            else:
                i = 0
                ans += 1
                while 0 <= y+i < N and 0<= x < M and board[y+i][x] == '|':
                    vst[y+i][x] = True
                    i += 1
print(ans)