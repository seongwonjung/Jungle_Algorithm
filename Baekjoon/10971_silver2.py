import sys, copy, math
input = sys.stdin.readline
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
vst = [False]*n
rst = float('inf')
begin = 0

def TSP(start, vst, cnt, sum):
    global n, rst, W, begin
    if rst <= sum:
        return
    if cnt == n-1: # 종료 조건
        sum += W[start][begin]
        rst = min(sum, rst)
        return
    
    for i in range(n):
        if W[start][i] != 0 and not vst[i]: # 방문한 도시, 현재 도시는 방문하지 않음
            vst[i] = True
            TSP(i, vst, cnt+1, sum+W[start][i])
            vst[i] = False

for i in range(n):
    begin = i
    vst[i] = True
    TSP(i, vst, 0, 0)
    vst[i] = False
print(rst)