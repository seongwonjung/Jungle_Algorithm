import sys
input = sys.stdin.readline
n = int(input())
matrix = [tuple(map(int, input().split()))for _ in range(n)]

dp = [[float('inf')]*(n)for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for length in range(2, n+1):    # 부분 행렬길이 2 ~ n
    for i in range(n-length+1): # 시작 인덱스 i (끝 인덱스 j가 범위를 넘지 않게 제한)
        j = i + length - 1      # 끝 인덱스 j
        
        for k in range(i, j):
            cost = matrix[i][0]*matrix[k][1]*matrix[j][1] + dp[i][k] + dp[k+1][j]
            if dp[i][j] > cost:
                dp[i][j] = cost

print(dp[0][n-1])