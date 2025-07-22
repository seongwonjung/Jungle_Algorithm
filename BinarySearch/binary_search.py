lst = [1, 35, 45, 56, 73, 83, 93, 456, 579]
start = 0
end = len(lst)-1
key = 56
idx = 0

def binary_search(start, end, key):
    mid = 0
    while(start < end):         # 종료 조건 -> 탐색 범위를 넘을 경우
        mid = (start+end)//2
        if lst[mid] == key:     # 종료 조건 -> 키 값을 찾은 경우
            break
        elif lst[mid] > key:    # 키 값이 더 작다면 start ~ mid-1
            end = mid - 1
        else:                   # 키 값이 더 크다면 mid+1 ~ end
            start = mid + 1
    return mid

print(binary_search(start, end, 579))
        
# def binary_search(start, end, key):
#     mid = (start+end)//2
#     if start > end:           # 종료 조건 -> 탐색 범위를 넘을 경우
#         return 
    
#     print(start, mid ,end)
#     if lst[mid] == key:       # 종료 조건 -> 키 값을 찾은 경우
#         print(mid)
#         return mid
#     elif lst[mid] > key:      # 키 값이 더 작다면 start ~ mid-1
#         return binary_search(start, mid-1, key)   
#     else:                     # 키 값이 더 크다면 mid+1 ~ end
#         return binary_search(mid+1, end, key)


# key = int(input("찾을 key값 입력: "))
# idx = 0
# idx = binary_search(start, end, key)
# print(f"{key}는 lst[{idx}] 입니다")