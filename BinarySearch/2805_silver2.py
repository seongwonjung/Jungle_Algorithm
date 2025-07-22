import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 자른 나무의 합 >= m
max_tree = max(arr)
def binary_search(start, end):
    h = (start+end)//2
    # 자른 나무들 더해주기
    total = 0
    for i in arr:
        if(i - h) > 0:
            total += i-h
            
    if start > end:
        return h
    
    if(total == m):
        return h
    elif(total > m):
        return binary_search(h+1, end)
    else:
        return binary_search(start, h-1)
    
rst = binary_search(0, max_tree)
print(rst)