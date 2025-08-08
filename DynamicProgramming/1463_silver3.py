import sys
input = sys.stdin.readline
x = int(input())
dp = [0]*(x+1)
for i in range(2, x+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[x])
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
# x = int(input())
# dp = [-1]*(x+1)
# def make_one(x):
#     if dp[x] != -1:
#         return dp[x]
#     if x == 1:
#         return 0
#     cnt = make_one(x-1) + 1
#     if x % 3 == 0:
#         cnt = min(cnt, make_one(x//3)+1)
#     if x % 2 == 0:
#         cnt = min(cnt, make_one(x//2)+1)
#     dp[x] = cnt
#     return dp[x]
# make_one(x)
# print(dp[x])