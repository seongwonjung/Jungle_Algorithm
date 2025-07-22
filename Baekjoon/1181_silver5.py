import sys
input = sys.stdin.readline

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    rst = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if len(left[i]) < len(right[j]):
            rst.append(left[i])
            i += 1
        elif len(left[i]) > len(right[j]):
            rst.append(right[j])
            j += 1
        else:
            if left[i] < right[j]:
                rst.append(left[i])
                i += 1
            else:
                rst.append(right[j])
                j += 1
    rst.extend(left[i:])
    rst.extend(right[j:])
    return rst
            
n = int(input())
# set -> list 로 중복제거
words = list(set(input() for _ in range(n)))
rst = merge_sort(words)
for word in rst:
    print(word.strip())






# words = sorted(words)
# words = sorted(words, key=len)

# for s in words:
#     print(s.strip())