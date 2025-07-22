# M = 사대의 개수, N = 동물의 수, L = 총의 사정거리
# 사대의 위치 X = [x1,x2,...] (m크기)
# 각 동물이 사는 위치(a1,b1),(a2,b2), ... animals
import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
X = sorted(map(int, input().split()))
animals = sorted([list(map(int, input().split())) for _ in range(N)])

# 동물 (n)만큼 순차적으로
# 이 동물이 사정거리 안에 있는지 찾고, 안에 있으면 rst += 1
# 동물과 가장 가까운 사대 찾기. x 값을 기준으로 가장 가까운 사대를 찾고
# if abs(x-a) + b <= L 인 경우가 rst += 1


for i in range(N):
    # if animals[i] 를 cnt += 1 해도되는지
    pass



print(animals)