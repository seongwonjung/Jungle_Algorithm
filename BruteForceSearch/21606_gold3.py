# 아침 산책
import sys
input = sys.stdin.readline
n = int(input().strip())
tree = input().strip()
tree = [int(i)for i in tree]
graph = [[]for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vst = [False]*(n+1)
rst = 0
def dfs(start, x):
    global rst
    if not vst[x]:
        vst[x] = True
    if x != start and tree[x-1] == 1:
        rst += 1
        return
    for y in graph[x]:
        if not vst[y]:
            vst[y] = True
            dfs(start, y)
            vst[y] = False

for i in range(n):
    if tree[i] == 1:
        dfs(i+1, i+1)
        vst = [False]*(n+1)
print(rst)