n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))

def binary_search(start, end, key):
    mid = (start+end)//2
    if(start > end):
        return False
    if(A[mid] == key):
        return True
    elif(A[mid] < key):
        return binary_search(mid+1, end, key)
    else:
        return binary_search(start, mid-1, key)

for i in range(m):
    if binary_search(0, n-1, B[i]):
        print(1)
    else:
        print(0)