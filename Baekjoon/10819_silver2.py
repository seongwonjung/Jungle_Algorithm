import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
rst = []
vst = [False]*n
def backtrackking(select_numbers):
    global arr, vst, n, rst
    # 종료 조건 
    if len(select_numbers) == n:
        sum = 0
        for i in range(1, n):
            sum += abs(select_numbers[i-1] - select_numbers[i])
        rst.append(sum)
        return
    
    for i in range(n):
        if not vst[i]:
            vst[i] = True
            select_numbers.append(arr[i])
            backtrackking(select_numbers)
            vst[i] = False
            select_numbers.pop()
            
backtrackking([])     
rst = max(rst)
print(rst)