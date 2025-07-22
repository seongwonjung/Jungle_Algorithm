import sys
input = sys.stdin.readline

def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i
        while(j > 0 and arr[j-1] > tmp):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = tmp
    return arr
n = int(input())
arr = [int(input()) for _ in range(n)]
insertion(arr)
for num in arr:
    print(num)
