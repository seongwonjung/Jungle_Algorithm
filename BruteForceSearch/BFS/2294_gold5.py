import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input())for _ in range(N)]
dist = [-1]*(K+1)
q = deque()
dist[0] = 0
q.append(0)
while q:
    cur = q.popleft()
    
    for c in coins:
        nxt = c + cur
        if nxt > K or dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)
        if nxt == K:
            print(dist[nxt])
            sys.exit(0)
print(-1)