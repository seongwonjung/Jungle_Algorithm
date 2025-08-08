from collections import deque
graph = [[] for _ in range(9)]
visited = [False]*9

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while(q):
        x = q.popleft()
        print(f"{x} ", end='')
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# 노드 1에 연결된 노드
graph[1].extend([2, 3, 8])
# 노드 2
graph[2].extend([1, 7])
# 노드 3
graph[3].extend([1, 4, 5])
# 노드 4
graph[4].extend([3, 5])
# 노드 5
graph[5].extend([3, 4])
# 노드 6
graph[6].append(7)
# 노드 7
graph[7].extend([2, 6, 8])
# 노드 8
graph[8].extend([1, 7])

bfs(1)