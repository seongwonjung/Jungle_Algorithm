graph = [[] for _ in range(9)]
visited = [False]*9

def bfs(start):
    q = list()  # 큐
    q.append(start) # 첫 노드를 큐에 삽입
    visited[start] = True   # 첫 노드를 방문 처리
    
    # 큐가 빌때까지 반복
    while(len(q) > 0):
        # 큐에서 하나의 원소를 뽑아 출력
        x = q[0]
        q.pop(0)
        print(f"{x} ", end='')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(len(graph[x])):
            y = graph[x][i]
            if not visited[y]:
                q.append(y)
                visited[y] = True

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