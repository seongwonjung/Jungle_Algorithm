def merge_sort(arr):
    n = len(arr)
    if n == 1:      # 더 이상 나눌 수 없음
        return arr
    mid = n//2
    # divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # left와 right 로 나누고 merge(합병)
    return merge(left, right)
    
def merge(left, right):
    l = r = 0
    rst = []
    # conquer + combine
    # left와 right의 맨 앞 원소들을 비교하며 rst 에 합병
    while(l  < len(left) and r < len(right)):
        if left[l] < right[r]:
            rst.append(left[l])
            l += 1
        else:
            rst.append(right[r])
            r += 1
    # 다 넣어지지 않은 원소들을 rst 에 넣어준다
    rst.extend(left[l:])
    rst.extend(right[r:])
        
    return rst

arr = list([6,4,1,7,3,9,8])
arr = merge_sort(arr)
print(arr)


# def merge_sort(arr):
#     n = len(arr)
#     if n == 1:
#         return arr
#     mid = n//2
    
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     rst = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             rst.append(left[i])
#             i += 1
#         else:
#             rst.append(right[j])
#             j += 1 
    
#     rst.extend(left[i:])
#     rst.extend(right[j:])
#     return rst

# arr = list([6,4,1,7,3,9,8])
# arr = merge_sort(arr)
# print(arr)