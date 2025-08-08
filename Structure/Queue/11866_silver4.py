import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
que = deque(i for i in range(1, n+1))
rst = []
i = 0
while(que):
    i += 1
    if i % k == 0:
        rst.append(que.popleft())
        continue
    que.append(que.popleft())
    
# < , > 출력 어떻게 하는지 몰라서 찾아봄
print("<"+", ".join(map(str,rst)) + ">")