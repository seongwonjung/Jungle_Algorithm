import sys
input = sys.stdin.readline
n, s = map(int, input().split())
items = list(map(int, input().split()))
cnt = 0
# 1. 재귀 DFS(백트래킹)으로 풀어보자
# def dfs(start, total, path=[]):
#     global cnt
#     if total == s and path != []:
#         cnt += 1

#     for i in range(start, n):
#             dfs(i+1, total+items[i], path+[items[i]])
# dfs(0,0)
# print(cnt)

# 2. 비트마스킹으로 풀어보자
def bit_mask(items):
    global cnt
    for mask in range(1 << n):
        subsets = [items[i] for i in range(n) if mask & (1 << i)]
        if sum(subsets) == 0 and subsets != []:
            cnt += 1
    return
bit_mask(items)
print(cnt)