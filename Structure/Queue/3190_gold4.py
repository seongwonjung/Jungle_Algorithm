# 보드 크기 = n*n
# 사과 개수 = k
# 사과 위치 x, y
# 방향 전환 횟수 = L
# x 초 뒤에 D 방향으로 전환
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
k = int(input().strip())
# apple = list(map(int, input().strip().split())for _ in range(k)) 틀린 문법
# apple = [tuple(map(int, input().strip().split())) for _ in range(k)]
apple = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
## ***** 사과 위치를 -1씩 줄여서 저장 안해서 계속 틀림 ******
l = int(input().strip())

# commands = list(input().strip() for _ in range(l)) 틀린 방법임..
commands = []
for _ in range(l):
    t, c = input().strip().split()
    commands.append((int(t), c))


# q = deque([0,0]) -> q[0] = 0, q[1] = 0 이렇게 저장됨
q = deque([(0,0)])

# 오른쪽 아래 왼쪽 위 순서
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]
# 뱀은 0,0 에서 오른쪽 방향을 본 상태로 시작.
dir = 0
time = 0
j = 0
while(True):
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    x, y = q[-1]
        
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx,ny) in q:
        time += 1
        break
        # 끝내기
    
    q.append((nx, ny))
    
    if (nx, ny) in apple:  # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        apple.remove((nx, ny))
    else:   # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        q.popleft()
        
    time += 1
    
    # 방향 전환
    if j < l and time == commands[j][0]:
        if commands[j][1] == "D":   # 오른쪽
            dir = (dir+1)%4
        else:   # 왼쪽
            dir = (dir-1)%4
        j += 1

print(time)