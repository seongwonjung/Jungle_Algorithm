# import sys, heapq
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# # dijkstra는 인접 리스트를 쓴다.
# edge = [[]for _ in range(N+1)]
# INF = sys.maxsize
# dist = [INF]*(N+1)
# for _ in range(M):
#     a, b, c = map(int, input().split())
#     edge[a].append((c, b))
# start, end = map(int, input().split())
# heap = [[0,start]]
# dist[start] = 0
# while heap:
#     ew, ev = heapq.heappop(heap)
#     if dist[ev] != ew:
#         continue
#     for nw, nv in edge[ev]:
#         if dist[nv] > ew + nw:
#             dist[nv] = ew + nw
#             heapq.heappush(heap, (dist[nv], nv))

# print(dist[end])

# # import sys, heapq
# # input = sys.stdin.readline
# # INF = sys.maxsize
# # n = int(input())
# # m = int(input())
# # edge = [[]for _ in range(n+1)]
# # for _ in range(m):
# #     a, b, c = map(int, input().split())
# #     edge[a].append([c,b])
# # start, end = map(int, input().split())
# # dist = [INF]*(n+1)

# # heap = [[0, start]]
# # dist[start] = 0
# # while heap:
# #     ew, ev = heapq.heappop(heap)
# #     if dist[ev] != ew:
# #         continue
# #     for nw, nv in edge[ev]:
# #         if dist[nv] > ew + nw:
# #             dist[nv] = ew + nw
# #             heapq.heappush(heap, [dist[nv], nv])

# # print(dist[end])

import sys, heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
edges = [[]for _ in range(N+1)]
INF = sys.maxsize
dist = [INF]*(N+1)
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges[a].append([b, cost])

start, end = map(int,input().split())
dist[start] = 0
heap = [[0, start]]
while heap:
    ew, ev = heapq.heappop(heap)
    if ew != dist[ev]:
        continue
    for nv, nw in edges[ev]:
        if dist[nv] > nw + ew:
            dist[nv] = nw + ew
            heapq.heappush(heap, [dist[nv], nv])
print(dist[end])