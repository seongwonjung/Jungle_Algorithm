import sys
input = sys.stdin.readline
n = int(input())
# 퀸을 놓은 칸의 같은 행, 열에는 퀸을 놓을 수 없다.
# 퀸을 놓은 칸의 대각선에는 퀸을 놓을 수 없다.
# 퀸을 놓은 칸을 (x1, y1) 이라고 하고, 다음에 놓을칸을 (x2, y2) 라고 하면
# if abs(x1-x2) == abs(y1-y2) 인 경우 대각선이다.
arr = [0]*n
vst = [False]*n
cnt = 0

def nqueen(depth, arr):
    global cnt
    if depth == n:
        cnt += 1
        return
    
    def chk(depth, i, arr): # 현재 확인하고자 하는 위치 = (depth, i)
        is_true = True
        for x in range(depth):
            if abs(depth-x) == abs(i-arr[x]):
                is_true = False
        return is_true
    
    for i in range(n):
        if not vst[i]:
            if chk(depth, i, arr):
                vst[i] = True
                arr[depth] = i
                nqueen(depth+1, arr)
                arr[depth] = 0
                vst[i] = False
            
nqueen(0, arr)
print(cnt)