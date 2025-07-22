import sys
input = sys.stdin.readline
N = int(input().strip())
paper = [list(map(int, input().strip().split())) for _ in range(N)]
# divide
# n//2 로 자른다. 크기가 1 이 될때까지 (모두 1 or 0 아니면) 자를때마다 +1 해주면 되려나
# n크기가 작아서 될 듯
# 그럼 먼저 전체 크기부터 전부 1 or 0인지 체크하고 자른다.
cnt_one = 0; cnt_zero = 0
def is_all_same(arr):
    tmp = arr[0][0]
    for row in arr:
        for i in row:
            if tmp != i:
                return -1
    return tmp
def cut(arr):
    global cnt_one, cnt_zero
    n = len(arr)
    oz = is_all_same(arr)
    if oz == 0:
        cnt_zero += 1
        return
    if oz == 1:
        cnt_one += 1
        return
    if n > 0:
        cut([row[:n//2] for row in arr[:n//2]])
        cut([row[n//2:] for row in arr[:n//2]])
        cut([row[:n//2] for row in arr[n//2:]])
        cut([row[n//2:] for row in arr[n//2:]])
    
cut(paper)
print(cnt_zero)
print(cnt_one)