import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
orders = list(map(int, input().split()))
qs = [deque()for _ in range(K+1)]

for i in range(K):
    qs[orders[i]].append(i)

outlet = []
ans = 0
for i in range(K):
    device = orders[i]
    # 크게 두 가지 경우로 나뉜다.
    # 1. 이미 꽂혀있는 제품인 경우, 2. 안 꽂혀있는 제품인 경우
    if device in outlet: # 1. 이미 꽂혀있는 제품인 경우
            qs[device].popleft()
            continue
    else:   # 2. 안 꽂혀있는 제품인 경우
            # 이때 두 가지로 나뉜다.
            # 2-1. 꽂을 곳이 남아있는 경우
            # 2-2. 꽂을 곳이 남아있지 않은 경우
        if len(outlet) < N: # 2-1. 꽂을 곳이 남아있는 경우
            outlet.append(device)
            qs[device].popleft()
        else:   # 2-2. 꽂을 곳이 남아있지 않은 경우
            tmp = []
            for j in outlet:
                if not qs[j]:   # 만약 j물건이 비어 있다면 = 다음에 쓰지 않으면
                    tmp.append([float('inf'), j])
                else:
                    tmp.append([qs[j][0], j])
            # tmp에서 가장 큰 값(가장 늦게 사용하는 물건)을 빼자
            order, rm_device = max(tmp, key=lambda x: x[0])
            outlet.remove(rm_device)
            # print(f"{rm_device}번 물건을 빼고, {device}번 물건을 넣는다")
            outlet.append(device)
            qs[device].popleft()
            ans += 1
    # print(outlet)
print(ans)