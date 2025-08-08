import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
q = deque(i for i in range(1, n+1))
while len(q) != 1:
    # 1. 맨 앞의 원소를 뺀다
    q.popleft()
    # 2. 맨 앞의 원소를 맨 뒤에 넣어준다
    q.append(q.popleft())

# 1.2.과정을 카드가 하나 남을때까지 반복
print(*q)