import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
INF = sys.maxsize
MAX_X = 100000
dist = [INF]*(MAX_X+1)
dq = deque()
dq.append(n)
dist[n] = 0
dx = [1,-1, 2]
while dq:
    x = dq.popleft()
    cost = dist[x]
    if x == k:
        print(cost)
        break

    for i in range(3):
        if i == 2:  
            nx = x*dx[i]
            new_cost = cost
        else:    
            nx = x+dx[i]
            new_cost = cost + 1
        if 0 <= nx <= MAX_X:
            if dist[nx] > new_cost:
                dist[nx] = new_cost
                if i == 2:
                    dq.appendleft(nx)
                else:
                    dq.append(nx)