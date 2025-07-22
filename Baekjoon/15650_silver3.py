# 1. 중복 없이 뽑아야함
# 2. 오름차순으로 출력
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
vst = [False]*(n+1)
def backtrackking(depth):
    if depth == m:
        return
    for i in range(1, n+1):
        if(not vst[i]):
            vst[i] = True
            arr.append(i)
            backtrackking(depth+1)
            vst[i] = False
            arr.pop()
            
backtrackking(0)