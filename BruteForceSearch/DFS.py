import sys
visited = [False]*9
graph = [[0]*1 for _ in range(9)]
def dfs(x):
    visited[x] = True
    print(f"{x} ", end='')
    for i in range(1, len(graph[x])): # 인접한 노드 사이즈만큼 탐색
        y = graph[x][i]
        if not visited[y]: # 방문하지 않았으면 즉 visited가 False일 때 not을 해주면 True가 되므로 아래 dfs 실행
            dfs(y)
        
graph[1].extend([2, 3, 8])

graph[2].extend([1, 7])

graph[3].extend([1, 4, 5])

graph[4].extend([3, 5])

graph[5].extend([3, 4])

graph[6].extend([7])

graph[7].extend([2, 6, 8])

graph[8].extend([1, 7])


dfs(1)