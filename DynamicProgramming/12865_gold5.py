import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# 물건을 담기 or 담지 않기 두 가지 경우가 있을 수 있다.
# 물건을 담는다면 배낭의 용량이 용량-weight(물건의 무게) 만큼 줄어든다.
# 물건을 담아서 줄어든 용량-weight 일 때에 대해서도 담거나, 담지 않거나 두 경우로 나뉜다.
# 따라서 용량 w라고 할 때 w-weight 에 대해서 dp로 중복되는 값을 저장할 수 있다-> dp로 풀이가능
# dp = [w][i] -> 남은 용량이 w, i번째 물건까지 담았을때의 최대값이라고 정의한다면
# 크기는 w = 0 ~ k, i = 1 ~ N가 된다.
dp = [[0]*(N+1)for _ in range(K+1)]
# (무게, 가치)
things = [tuple(map(int, input().split()))for _ in range(N)]
for w in range(1, K+1):
    for i in range(1, N+1):
        weight, value = things[i-1]
        if w < weight:  # 물건의 무게가 용량을 초과할 땐 가방에 담지 못한다.
            dp[w][i] = dp[w][i-1]
        else:   # 담을 수 있을땐 담기 or 담지 않기 두 가지 경우가 생긴다.
                # 둘 중 더 큰 값을 dp[i][w] 에 넣는다
            dp[w][i] = max(dp[w][i-1], dp[w-weight][i-1]+value)
print(dp[K][N])













# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# stuff = [[0,0]]
# for i in range(1, N+1):
#     W, V = map(int, input().split())
#     stuff.append([W, V]) # 무게, 가치
    
# dp = [[0]*(N+1) for _ in range(K+1)]

# for i in range(1, N+1):
#     for w in range(1, K+1):
#         weight, cost = stuff[i]
#         if w < weight:
#             dp[w][i] = dp[w][i-1]
#         else:
#             dp[w][i] = max(dp[w][i-1], cost + dp[w-weight][i-1])

# print(dp[K][N])