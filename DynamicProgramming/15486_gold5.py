import sys
input = sys.stdin.readline
n = int(input())
schedule = [list(map(int, input().split()))for _ in range(n)]
dp = [0]*(n+1)
for i in range(n):
    time, pay = schedule[i]
    dp[i+1] = max(dp[i], dp[i+1])
    if i + time <= n:
        dp[i+time] = max(dp[i+time], dp[i]+pay)

print(dp[n])