import sys
input = sys.stdin.readline
str_a = input().strip()
str_b = input().strip()
# a, b 의 각각의 끝 부분을 i, j 라고 하자
# str_a[i] == str_b[j] 라면? dp[i-1][j-1] + 1
# 다르다면?
# dp[i][j] = dp[i-1][j] or dp[i][j-1]
N, M = len(str_a), len(str_b)
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if str_a[i-1] == str_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[N][M])