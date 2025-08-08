import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
vst = [False]*(n+1)

def dfs(x):
    vst[x] = True
    print(f"{x}", end=' ')
    for y in graph[x]:
        if not vst[y]:
            dfs(y)
    
def bfs(start):
    q = deque()
    q.append(start)
    vst[start] = True
    while(q):
        x = q.popleft()
        print(f"{x}", end=' ')
        for y in graph[x]:
            if not vst[y]:
                q.append(y)
                vst[y] = True
                
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for abj in graph:
    abj.sort()
dfs(v)
vst = [False]*(n+1)
print()
bfs(v)