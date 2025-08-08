# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# n, m = map(int, input().split())
# graph = [[]for _ in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# chk = [False]*(n+1)
# def dfs(x):
#     if not chk[x]:
#         chk[x] = True
#     for y in graph[x]:
#         if not chk[y]:
#             dfs(y)
# rst = 0
# for i in range(1, n+1):
#     if not chk[i]:
#         dfs(i)
#         rst += 1
# print(rst)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

vst = [False]*(N+1)
def dfs(v):
    vst[v] = True
    for nv in graph[v]:
        if not vst[nv]:
            dfs(nv)
rst = 0
for i in range(1, N+1):
    if not vst[i]:
        rst += 1
        dfs(i)
print(rst)