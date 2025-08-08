# # Kruskal 을 이용한 풀이
# # Kruskal 에서 가장 중요한 것은 parent 배열을 만들고
# # 각 노드의 루트 노드를 parent에 넣는다. 
# # 만약 parent가 같은 노드를 가리킨다면 그 노드들은 집합으로 연결되어 있다. find
# # 연결되어 있지 않다면, union을 통해 합쳐준다.
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# INF = sys.maxsize
# V, E = map(int, input().split())
# edges = []
# for _ in range(E):
#     a, b, cost = map(int, input().split())
#     edges.append([cost,a,b])

# edges.sort()
# parent = [i for i in range(V+1)]
# # find
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
# # union
# def union(a, b):
#     a_root = find(a)
#     b_root = find(b)
#     if a_root != b_root:
#         parent[b_root] = a_root
#         return True
#     return False

# total_cost = 0
# for cost, a, b in edges:
#     if union(a,b):
#         total_cost += cost
# print(total_cost)



# prim 을 이용한 풀이
# import sys, heapq
# input = sys.stdin.readline
# V, E = map(int, input().split())
# # 인접 리스트 edge
# # 방문체크용 리스트 chk 
# edge = [[] for _ in range(V+1)]
# chk = [False]*(V+1)
# rst = 0
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     edge[a].append([c, b])
#     edge[b].append([c, a])

# heap = [[0,1]]
# while heap:
#     w, each_node = heapq.heappop(heap)
#     if not chk[each_node]:
#         chk[each_node] = True
#         rst += w
#         for next_node in edge[each_node]:
#             if not chk[next_node[1]]:
#                 heapq.heappush(heap, next_node)
# print(rst)

import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split())
edges = [[]for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([c, b])
    edges[b].append([c, a])
chk = [False]*(V+1)
heap = [[0,1]]
rst = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if not chk[ev]:
        chk[ev] = True
        rst += ew
        for nw, nv in edges[ev]:
            if not chk[nv]:
                heapq.heappush(heap, [nw, nv])
print(rst)