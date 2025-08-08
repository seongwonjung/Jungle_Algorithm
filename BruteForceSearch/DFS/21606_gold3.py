import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
# 1 = 실내, 0 = 실외
A = list(map(int, input().strip()))
edges = [[]for _ in range(N+1)]
rst = 0
vst = [False]*(N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    if A[a-1] == 1 and A[b-1] == 1:
        rst += 2
# 실내 - 실내 인 경우 +2를 바로 해준다.
# 실외(0)을 기준으로 몇개 있는지 세준다.
# if 실내 -> 실내로 가는 경로가 있다면
# 현재 실외와 연결된 실내 개수 리턴
def dfs(x):
    vst[x] = True
    cnt = 0
    for y in edges[x]:
        if A[y-1] == 1:
            cnt += 1
        elif not vst[y]:
            cnt += dfs(y)
    return cnt

for i in range(1, N+1):
    if A[i-1] == 0 and not vst[i]:
        cnt = dfs(i)
        rst += cnt*(cnt-1)
print(rst)