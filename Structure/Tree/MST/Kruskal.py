# 최소 신장 트리를 구성하는 크루스칼 알고리즘
# Union-Find (Disfoint Set)을 이용해 사이클 방지

# 간선 정보: (비용, 정점1, 정점2)
edges = [
    (1, 'A', 'B'),
    (3, 'A', 'D'),
    (3, 'B', 'C'),
    (6, 'B', 'D'),
    (4, 'C', 'D'),
    (2, 'C', 'E'),
    (5, 'D', 'E')
]

# 모든 정점 추출
nodes = set()
for cost, u, v in edges:
    nodes.add(u)
    nodes.add(v)

# 부모 테이블 초기화
parent = {node: node for node in nodes}

# find 연산: 루트 노드를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])     # 경로 압축
    return parent[x]

# union 연산: 두 집합을 합침
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x     # 하나로 합침

# 크루스칼 알고리즘 실행
mst = []
total_cost = 0

# 간선을 비용 기준으로 정렬
edges.sort()

for cost, u, v in edges:
    # 사이클이 생기지 않는다면 MST 에 포함
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, cost))
        total_cost += cost
        
# 결과 출력
print("MST 간선 목록:")
for u, v, cost in mst:
    print(f"{u} - {v} ({cost})")

print("총 비용:", total_cost)