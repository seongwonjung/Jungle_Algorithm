import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split()))for _ in range(N)]
    rank.sort()
    rst = [rank[0]]
    for a, b in rank[1:]:
        if b < rst[-1][1]:
            rst.append([a, b])
    print(len(rst))