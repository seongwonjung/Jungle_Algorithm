import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
K = int(input())
# 정점의 집합을 둘로 분할하여, 
# 같은 집합인 정점끼리 인접하지 않도록 분할할 수 있을 때 -> 이분 그래프 라고 부른다.
# KeyPoint = 그룹 -1, 1과 있다고 하면 -1 다음 노드는 1이 와야한다.
def dfs(v, group):
    chk[v] = group
    for nxt in graph[v]:
        if chk[nxt] == 0:
            if not dfs(nxt, -group):    # 이 부분 잘 보자. 처음엔 그냥 dfs(nxt, -group)만 써서 return 값이 항상 True로 됐음
                return False
        elif chk[nxt] == group:
            return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[]for _ in range(V+1)]
    chk = [0]*(V+1)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    success = True
    for i in range(1, V+1):
        if chk[i] == 0:
            success = dfs(i, 1)
            if not success:
                break
    print("YES") if success else print("NO")

    

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# K = int(input().strip())
# # 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때
# def dfs(x, vst, graph, group):
#     vst[x] = group
#     for y in graph[x]:
#         if vst[y] == 0:
#             rst = dfs(y, vst, graph, -group)
#             if not rst:
#                 return False
#         else:
#             if vst[y] == group:
#                 return False
#     return True
    
# for _ in range(K):
#     V, E = map(int, input().strip().split())
#     #  각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
#     vst = [0]*(V)
#     # 0 = 방문하지 않음, 1, -1 로 반전시키며 이전 노드와 같은 group인지 비교
#     graph = [[] for _ in range(V)]
#     for _ in range(E):
#         u, v = map(int, input().strip().split())
#         graph[u-1].append(v-1)
#         graph[v-1].append(u-1)
    
#     for i in range(V):
#         if vst[i] == 0:
#             rst = dfs(i, vst, graph, 1)
#         if not rst:
#             break
#     print("YES") if rst else print("NO")