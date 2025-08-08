import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
E = int(input())
edge = [[]for _ in range(N+1)]
vst = [False]*(N+1)
for _ in range(E):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
rst = 0
def dfs(x):
    global rst
    vst[x] = True
    for nxt in edge[x]:
        if not vst[nxt]:
            dfs(nxt)
            rst += 1
dfs(1)
print(rst)

# import sys
# from collections import deque
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# computer = int(input())
# e = int(input())
# graph = [[]for _ in range(computer+1)]
# for _ in range(e):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def dfs(x):
#     vst = [False]*(computer+1)
#     stack = [x]
#     vst[x] = True
#     rst = 0
#     while stack:
#         x = stack.pop()
#         for y in graph[x]:
#             if not vst[y]:
#                 rst+=1
#                 stack.append(y)
#                 vst[y] = True
#     return rst
# print(dfs(1))
# def bfs(start):
#     vst = [False]*(computer+1)
#     q = deque()
#     q.append(start)
#     vst[start] = True
#     rst = 0
#     while(q):
#         x = q.popleft()
#         for y in graph[x]:
#             if not vst[y]:
#                 rst += 1
#                 q.append(y)
#                 vst[y] = True
                
#     return rst
# print(bfs(1))