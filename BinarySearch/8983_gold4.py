# M = 사대의 개수, N = 동물의 수, L = 총의 사정거리
# 사대의 위치 X = [x1,x2,...] (m크기)
# 각 동물이 사는 위치(a1,b1),(a2,b2), ... animals
import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
X = sorted(map(int, input().split()))
animals = sorted([list(map(int, input().split())) for _ in range(N)])
animals = [a for a in animals if a[1] <= L] # 사정 거리 보다 멀리 있는 동물 빼줌
rst = 0
# 동물 (n)만큼 순차적으로
# 이 동물이 사정거리 안에 있는지 찾고, 안에 있으면 rst += 1
# 동물과 가장 가까운 사대 찾기. x 값을 기준으로 가장 가까운 사대를 찾고
# if abs(x-a) + b <= L 인 경우가 rst += 1
def is_targetable(a, b, x):
    if abs(x-a) + b <= L:
        return True
    else:
        return False
    
def binary_search(s, e, animal):
    a, b = animal
    while(s <= e):
        mid = (s+e)//2
        if is_targetable(a,b,X[mid]):
            return True
        if a > X[mid]:
            s = mid+1
        else:
            e = mid-1
    return False

for i in animals:
    if binary_search(0, M-1, i):
        rst += 1
print(rst)