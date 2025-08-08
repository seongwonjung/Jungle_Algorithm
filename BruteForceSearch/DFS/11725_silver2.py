import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 1이 root 로 고정임 내려가면서 parent[nxt]=v 
N = int(input())
edge = [[]for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
parent = [0]*(N+1)
parent[1] = 1
def dfs(v = 1):
    for nxt in edge[v]:
        if parent[nxt] == 0:
            parent[nxt] = v
            dfs(nxt)
dfs(1)
for i in range(2, N+1):
    print(parent[i])

# DFS 로 풀어보자
# 처음 1 로 시작. 1로 갈수 있는 애들은 다 parent 가 1
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
parent = [0]*(n+1)
parent[1] = 1
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    for y in graph[x]:
        if parent[y] == 0:
            parent[y] = x
            dfs(y)
            
dfs(1)
for i in range(2, n+1):
    print(parent[i])