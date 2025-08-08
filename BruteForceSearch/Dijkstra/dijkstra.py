"""
1. 아이디어
- 한점시작, 모든 거리 : 다익스트라
- 간선, 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들 수행
    - 최신값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- 다익스트라 : O(ElgV)
"""
# import sys, heapq, math
# input = sys.stdin. readline
# V, E = map(int, input().split())
# K = int(input())
# INF = math.inf
# edge = [[] for _ in range(V+1)]
# dist = [INF] * (V+1)
# for i in range(E):
#     u,v,w = map(int, input().split())
#     edge[u].append([w,v])

# # 시작점 초기화
# dist[K] = 0
# heap = [[0,K]]

# while heap:
#     ew, ev = heapq.heappop(heap)
#     if dist[ev] != ew:  continue
#     for nw, nv in edge[ev]:
#         if dist[nv] > ew + nw:
#             dist[nv] = ew + nw
#             heapq.heappush(heap, [dist[nv], nv])

# for i in range(1, V+1):
#     if dist[i] == INF: print("INF")
#     else:   print(dist[i])

import heapq, math

def dijkstra(start, graph, n):
    INF = math.inf # 무한대 값 (도달할 수 없는 노드를 표현하기 위해 사용)
    distance = [INF]*(n+1)  # 최단 거리 테이블 초기화 (1번 노드부터 n번 노드까지)
    distance[start] = 0 # 시작 노드까지의 거리는 0으로 설정
    
    h = []
    heapq.heappush(h, (0, start))   # 힙 푸시 (거리, 노드)
    
    while h:
        dist, now = heapq.heappop(h)    # 현재 최단 거리가 가장 짧은 노드르 꺼냄
        
        # 이미 처리된 적 있는 노드라면 무시(더 짧은 거리로 방문한 적 있음)
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 인접 노드들을 확인
        for neighbor, weight in graph[now]:
            cost = dist + weight    # 현재 노드를 거쳐서 가는 거리 계산
            # 기존에 기록된 거리보다 더 짧은 경로가 있다면 갱신
            if cost < distance[neighbor]:
                distance[neighbor] = cost   # 거리 테이블 업데이트
                heapq.heappush(h, (cost, neighbor)) # 큐에 새로운 거리로 삽입
        
    return distance     # 모든 노드까지의 최단 거리 반환 (1~n번 노드까지)