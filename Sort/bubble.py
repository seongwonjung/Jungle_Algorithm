# 기본 버블 정렬
def bubble(arr, ccnt, scnt):
    n = len(arr)
    for i in range(n-1):    # n-1번 pass -> 마지막 원소는 이미 끝에 놓여있음
        for j in range(n-1, i, -1):
            ccnt += 1
            if(arr[j-1] > arr[j]):  # 이웃한 두 원소의 대소 비교
                scnt += 1
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr, ccnt, scnt 

arr = list([6,4,3,7,1,9,8])
ccnt = 0    # 비교횟수
scnt = 0    # 교환횟수
arr, ccnt, scnt = bubble(arr, ccnt, scnt)
print(arr)
print(f"비교 횟수 : {ccnt} 교환 횟수 : {scnt}")

# 교환이 한번도 안일어나면 -> 이미 정렬이 완료되면 종료
# def bubble(arr, ccnt, scnt):
#     n = len(arr)
#     for i in range(n-1):    # n-1번 pass -> 마지막 원소는 이미 끝에 놓여있음
#         exchange = 0
#         for j in range(n-1, i, -1):
#             ccnt += 1
#             if(arr[j-1] > arr[j]):  # 이웃한 두 원소의 대소 비교
#                 exchange += 1
#                 scnt += 1
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#         if exchange == 0:
#             break
#     return arr, ccnt, scnt 

# arr = list([6,4,3,7,1,9,8])
# ccnt = 0    # 비교횟수
# scnt = 0    # 교환횟수
# arr, ccnt, scnt = bubble(arr, ccnt, scnt)
# print(arr)
# print(f"비교 횟수 : {ccnt} 교환 횟수 : {scnt}")

# 정렬된 부분 스캔 범위에서 제외
# def bubble(arr, ccnt, scnt):
#     n = len(arr)
#     k = 0
#     while(k < n-1):
#         last = n-1  # 마지막으로 교환이 일어난 곳을 담을 변수
#         for j in range(n-1, k, -1):
#             ccnt += 1
#             if(arr[j-1] > arr[j]):  # 이웃한 두 원소의 대소 비교
#                 scnt += 1
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 last = j    # 교환이 일어날때마다 last = j -> 마지막으로 교환이 일어난 위치가 담김
#             k = last
#     return arr, ccnt, scnt

# arr = list([1,3,9,4,7,8,6])
# ccnt = 0    # 비교횟수
# scnt = 0    # 교환횟수
# arr, ccnt, scnt = bubble(arr, ccnt, scnt)
# print(arr)
# print(f"비교 횟수 : {ccnt} 교환 횟수 : {scnt}")


# shaker sotr
# def bubble(arr, ccnt, scnt):
#     n = len(arr)
#     left = 0
#     right = n-1
#     last = right
#     while(left < right):
#         for j in range(right, left, -1):  # 홀수 패스 -> 가장 작은 원소를 맨 앞으로 이동시킴
#             ccnt += 1
#             if(arr[j-1] > arr[j]):
#                 scnt += 1
#                 arr[j], arr[j-1] = arr[j-1], arr[j]
#                 last = j
#         left = last
        
#         for j in range(left, right):   # 짝수 패스 -> 가장 큰 원소를 맨 뒤로 이동시킴
#             ccnt += 1
#             if(arr[j] > arr[j+1]):
#                 scnt += 1
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 last = j
#         right = last
#     return arr, ccnt, scnt 

# arr = list([9,1,3,4,6,7,8])
# ccnt = 0    # 비교횟수
# scnt = 0    # 교환횟수
# arr, ccnt, scnt = bubble(arr, ccnt, scnt)
# print(arr)
# print(f"비교 횟수 : {ccnt} 교환 횟수 : {scnt}")