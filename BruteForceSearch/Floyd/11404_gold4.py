import sys
input = sys.stdin.readline
# 플로이드 와샬
# 1. N*N INF 배열을 만든다
# 2. 자기자신으로 가는 곳은 0으로 초기화 (i,i)
# 3. i에서 j 로 갈 때, i -> k + k -> j (k를 거치는게) 더 빠르다면 갱신
N = int(input())
M = int(input())
INF = sys.maxsize
rs = [[INF]*(N+1)for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    # a -> b 로 가는 간선이 여러 개 있을 경우를 위해 min 값으로 넣어줌
    rs[a][b] = min(rs[a][b], c)

for i in range(1, N+1):    rs[i][i] = 0 

for k in range(1, N+1):
    for j in range(1, N+1):
        for i in range(1, N+1):
            rs[j][i] = min(rs[j][i], (rs[j][k] + rs[k][i]))

for i in range(1, N+1):
    for j in range(1, N+1):
        if rs[i][j] == INF:
            print(0, end=' ')
        else:
            print(rs[i][j], end=' ')
    print()


# """
# 1. 아이디어
# - 모든점 -> 모든점 : 플로이드
# - 비용배열 INF 초기화
# - 간선의 비용 대입
# - 거쳐서 비용 줄어들 경우, 갱신(for문 3번)

# 2. 시간복잡도
# - 플로이드 : O(V^3)
# - 1e6 > 가능
# """

# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# INF = sys.maxsize

# rs = [[INF]*(n+1) for _ in range(n+1)]

# for i in range(1, n+1):
#     rs[i][i] = 0

# for i in range(m):
#     a,b,c = map(int, input().split())
#     rs[a][b] = min(rs[a][b], c)

# for k in range(1, n+1):
#     for j in range(1, n+1):
#         for i in range(1, n+1):
#             rs[j][i] = min (rs[j][i], (rs[j][k] + rs[k][i]))
                
# for j in range(1, n+1):
#     for i in range(1, n+1):
#         if rs[j][i] == INF:
#             print("0", end=' ')
#         else:
#             print(rs[j][i], end=' ')
#     print()