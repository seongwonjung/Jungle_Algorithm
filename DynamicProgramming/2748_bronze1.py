import sys
input = sys.stdin.readline
n = int(input())
a, b = 0, 1
for _ in range(2, n+1):
    a, b = b, a+b
print(b)

# recursion 
# import sys
# input = sys.stdin.readline
# n = int(input())
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(n))

# Top-Down 방식
# import sys
# input = sys.stdin.readline
# n = int(input())
# memo = {}
# def fibonacci(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci(n-1) + fibonacci(n-2)
#     return memo[n]
# print(fibonacci(n))

# Bottom-Up 방식
# import sys
# input = sys.stdin.readline
# n = int(input())
# def fibonacci(n):
#     dp = [0]*(n+1)
#     dp[0], dp[1] = 0, 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     print(dp[n])
# fibonacci(n)