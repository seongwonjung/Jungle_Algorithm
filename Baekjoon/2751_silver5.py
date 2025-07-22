import sys
input = sys.stdin.readline
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    
def merge(left, right):
    result = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    # 아직 다 안 담긴 원소들 넣어줌
    result += left[i:]
    result += right[j:]
    return result    


n = int(input())
arr = [int(input()) for _ in range(n)]
arr = merge_sort(arr)
for num in arr:
    print(num)