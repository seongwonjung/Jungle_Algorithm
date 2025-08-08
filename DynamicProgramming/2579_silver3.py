import sys
input = sys.stdin.readline
n = int(input())
steps = [int(input()) for _ in range(n)]
dp = [0]*(n+1)
if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[1]+steps[0])
else:
    dp[1], dp[2] = steps[0], steps[0]+steps[1]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+steps[i-1], dp[i-3]+steps[i-1]+steps[i-2])
    print(dp[n])