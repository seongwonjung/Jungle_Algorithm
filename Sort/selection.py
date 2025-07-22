 
def simple_selection(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if(arr[min] > arr[j]):  # 가장 작은 원소의 인덱스 찾기
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        i += 1
    return arr
arr = list([6,4,8,3,1,9,7])
arr = simple_selection(arr)
print(arr)