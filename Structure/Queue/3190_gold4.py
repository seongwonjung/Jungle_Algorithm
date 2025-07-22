from collections import deque

N = int(input())
apple_cnt = int(input())
def map_init():
    maps = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(apple_cnt):
        x, y = map(int, input().split())
        maps[x - 1][y - 1] = 1
    return maps
maps = map_init()

que = deque((0, 0))
right_x = [1, 0, -1, 0]
right_y = [0, 1, 0, -1]

left_x = [-1, 0, 1, 0]
left_y = [0, 1, 0, -1]
nx = 0
ny = 0
game_time = 1
count = 1

command_cnt = int(input())
for _ in range(command_cnt):
    commands = input().split()
print(commands)
while que:
    print(que)
    x = que.popleft()
    y = que.popleft()
    
    if maps[x - 1][y - 1] == 1:
        que.append(x, y)

    if x >= N or y >= N or x < 0 or y < 0 or (x in que and y in que):
        count += 1
        break
    
    if int(commands[0]) == game_time:
        nx = (nx + 1) % 4
        ny = (ny + 1) % 4
        if commands[1] == 'D':
            print(x,  right_x[nx])
            que.append(x + right_x[nx])
            que.append(y + right_y[ny])
        elif commands[1] == 'L':
            que.append(x + left_x[nx])
            que.append(y + left_y[ny])
    else:
        que.append(x + right_x[nx])
        que.append(y + right_y[ny])
    
    game_time += 1
    count += 1

print(count)


# 보드 크기 = n*n
# 사과 개수 = k
# 사과 위치 x, y
# 방향 전환 횟수 = L
# x 초 뒤에 D 방향으로 전환함
# import sys
# input = sys.stdin.readline
# n = int(input().strip())
# k = int(input().strip())
# x, y = map(int, input().strip().split())
# l = int(input().strip())
# 뱀은 0,0 에서 오른쪽 방향을 본 상태로 시작.