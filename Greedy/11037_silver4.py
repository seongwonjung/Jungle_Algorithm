import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

cnt = 0
for i in range(len(coins)-1, -1, -1):
    if K == 0: break
    cnt += K//coins[i]
    K = K%coins[i]

print(cnt)