from collections import deque

def topology_sort(n, graph, indegree):
    rst = []
    q = deque()
    
    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        rst.append(now)
        
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    
    # 사이클이 있는 경우 확인용
    if len(rst) != n:
        print("사이클 발생(순서를 정할 수 없음)")
    else:
        print("위상 정렬 결과: ", *rst)

n, m = map(int, input().split())  # 노드 수, 간선 수
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)     # a → b
    indegree[b] += 1       # b의 진입차수 증가

topology_sort(n, graph, indegree)