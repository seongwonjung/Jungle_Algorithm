import sys
from collections import deque
input = sys.stdin.readline
N = int(input())    # 1 ~ n-1 = 기본 부품, 중간 부품 n = 완제품 번호
M = int(input())
graph = [[]for _ in range(N+1)]
indegree = [0]*(N+1)
need = [[0]*(N+1)for _ in range(N+1)]

for _ in range(M):
    # x를 만드는데 필요한 y가 k개 필요함
    x, y, k = map(int, input().split())
    graph[y].append([x, k])
    indegree[x] += 1
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        need[i][i] = 1

while q:
    now = q.popleft()
    for nxt, count in graph[now]:
        for i in range(1, N+1):
            need[nxt][i] += need[now][i]*count
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, N+1):
    if need[N][i] > 0:
        print(i, need[N][i])