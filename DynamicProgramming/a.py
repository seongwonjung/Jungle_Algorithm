import sys
input = sys.stdin.readline
n = int(input())
steps = list(int(input()) for _ in range(n))
dp = [0]*(n+1)
if n == 1:
    print(steps[0])
elif n == 2:
    print(steps[1]+steps[0])
else:
    dp[1], dp[2] = steps[0], steps[0] + steps[1]
    # dp[i] = i 번째 계단에서의 최대값
    for i in range(3, n+1):
        dp[i] = max(dp[i-2] + steps[i-1] , dp[i-3] + steps[i-2] +steps[i-1])
    print(dp[n])

# import sys
# input = sys.stdin.readline
# T = int(input())
# dp = [0]*(12)
# dp[1], dp[2], dp[3] = 1, 2, 4
# for i in range(4, 12):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# for _ in range(T):
#     x = int(input())
#     print(dp[x])

# import sys
# input = sys.stdin.readline
# x = int(input())
# dp = [0]*(x+1)
# for i in range(2, x+1):
#     dp[i] = dp[i-1]+1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3]+1)
# print(dp[x])

# import sys
# input = sys.stdin.readline
# n = int(input())
# a, b = 0, 1
# for i in range(2, n+1):
# 	a, b = b, a+b
# print(b)