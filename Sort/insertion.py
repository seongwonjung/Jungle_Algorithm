def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i
        # j가 0보다 크고, tmp가 정렬된 구간에서 더 작은 원소를 발견할때까지
        while(j > 0 and arr[j-1] > tmp): 
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = tmp
    return arr

arr = list([6,4,1,7,3,9,8])
arr = insertion(arr)
print(arr)