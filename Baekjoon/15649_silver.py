# 백트래킹 - 재귀를 이용 for문으로 n까지 하나씩 선택(이때 vst 체크필요)
# 선택한 숫자 담을 리스트 arr[]
# 방문여부 체크 vst[]
# 종료 조건 - depth = m 이 되었을떄
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
vst = [False]*(n+1)

def dfs(depth):
    if depth == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if not vst[i]:
            vst[i] = True
            arr.append(i)
            dfs(depth+1)
            vst[i] = False
            arr.pop()
dfs(0)