def quick_sort(arr, low=0, high=None):
    if(high == None):
        high = len(arr)-1
    if(low >= high):
        return
    
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    
    quick_sort(arr, low, i-1)
    quick_sort(arr, low+i, high)

arr = [42, 7, 89, 15, 63, 27, 38, 94, 56, 21]
quick_sort(arr)
print(arr)
# def quick_sort(arr):
#     # pivot 선택 -> arr[0] or arr[n//2]
#     # left(pivot 보다 작은), right(pivot 보다 큰) , equal(같은)로 나눈다 return left+equal+right
#     # if n <= 1 종료 return arr
#     n = len(arr)
#     if n <= 1:
#         return arr
#     pivot = arr[n//2]
#     left = [i for i in arr if i < pivot]
#     right = [i for i in arr if i > pivot]
#     return quick_sort(left) + [pivot] + quick_sort(right)
    
# arr = [42, 7, 89, 15, 63, 27, 38, 94, 56, 21]
# n = len(arr)
# arr = quick_sort(arr)
# print(arr)




# def quick_sort(arr, low = 0, high = None):
#     # divide 
#     # pivot 을 정하고 나누자
#     # pivot 보다 작은 값을 왼쪽에 넣고 오른쪽에 큰 값이 오도록
#     if high == None:
#         high = len(arr) - 1
#     if low >= high:
#         return
#     pivot = arr[high]
#     # i 는 마지막에 교환한 위치를 저장하기 위함
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot: # pivot보다 작은 값들을 왼쪽으로 밀어넣는다
#             i += 1
#             arr[j], arr[i] = arr[i], arr[j]
#             # i 의 위치를 계속해서 마지막에 바꾼 위치로 만들어준다
#     i += 1
#     # 마지막에 교환이 일어난 위치 뒤와 high값을 swap

#     arr[i], arr[high] = arr[high], arr[i]
    
#     quick_sort(arr, low+i, high)
#     quick_sort(arr, low, i-1)

# arr = [42, 7, 89, 15, 63, 27, 38, 94, 56, 21]
# quick_sort(arr)
# print(arr)

# low = 0, high = 9, pivot = 21
# i = -1
# 7(j==1) 일 때 교환이 일어남
# i+1 이므로 0 번인덱스와 1번인덱스 교환
# 7, 42, 89, 15, 63,....
# 15(j == 3 일때) 교환
# i+1 이므로 1번 인덱스와 3번 인덱스 교환
# 7, 15, 89, 42, 63, 27, 38, 94, 56, 21
# for 문이 끝나고
# (7, 15) , (89, 42, 63, 27, 38, 94, 56, 21) 가 pivot 기준으로 나눈 배열
# 마지막으로 i+1 후 arr[i]와 arr[high] 를 바꿔줌
# pivot보다 작은 값들을 왼쪽으로 다 밀었고 마지막으로 민 인덱스가 i이기 때문에
# i 인덱스 다음에 pivot 이 와야 함
# 7, 15, 21, 89, 42, 63, 27, 38, 94, 56
# 이 과정을 i(마지막 교환 위치)보다 큰 구간, 작은 구간을 나누어 반복
# quick_sort(arr, low+i, high)
# right = (89,42,63,27,38,94,56)
# quick_sort(arr, low, i-1)
# left = (7, 15)
# i 인덱스인 21 은 이미 정렬된 위치이기 때문에 제외된다.