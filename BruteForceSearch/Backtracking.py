import sys
input = sys.stdin.readline
n,m = map(int, input().split())
vst = [False]*(n+1)
arr = []

def dfs(depth):
    if depth == m:  # pruning 조건 -> m개 만큼 선택했으면 돌아감(더 선택할 필요 없음)
        print(*arr)
        return
    for i in range(1, n+1):
        if not vst[i]:
            vst[i] = True
            arr.append(i)
            dfs(depth+1)
            arr.pop()
            vst[i] = False

dfs(0)