# 배열을 이용한 방식
def counting(arr):
    max_value = max(arr)
    count = [0]*(max_value + 1)
    
    # 1. 각 숫자 세기
    for num in arr:
        count[num] += 1
    
    # 2. 누적합으로 변환
    for i in range(1, max_value+1):
        count[i] += count[i-1]
    print(count)
    
    # 3. 결과 배열
    result = [0]*len(arr)
    for num in arr:
        idx = count[num]
        result[idx-1] = num
        count[num] -= 1
    
    return result

arr = [6,4,1,7,3,9,8]
print(counting(arr))

# 딕셔너리를 사용한 방식
def counting_dict(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    result = []
    
    for num in range(max(arr)+1):
        while num in count_dict and count_dict[num] != 0:
            result.append(num)
            count_dict[num] -= 1
    
    return result

arr = [4, 7, 9, 1, 3, 5, 2, 3, 4]
print(counting_dict(arr))