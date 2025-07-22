# Knuth 수열
def shell_kunth(arr):
    n = len(arr)
    gap = 1
    while(gap < n): # Knuth 수열 생성
        gap = 3*gap+1
    while(gap > 0):
        for i in range(gap, n):
            j = i
            tmp = arr[i]
            while j >= gap and arr[j-gap] > tmp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = tmp
        gap //= 3
    return arr

arr = list([6,4,1,7,3,9,8])
print(shell_kunth(arr))    



# def shell(arr):
#     n = len(arr)
#     h = n // 2  # gap
#     while(h > 0):
#         for i in range(h, n):
#             j = i
#             tmp = arr[i]
#             while j >= h and arr[j-h] > tmp:
#                 arr[j] = arr[j-h]
#                 j -= h
#             arr[j] = tmp
#         h //= 2
        
#     return arr    

# arr = list([6,4,1,7,3,9,8])
# print(shell(arr))