import sys
input = sys.stdin.readline
n = int(input())
count = {}
max_val = 0
for i in range(n):
    num = int(input())
    max_val = max(num, max_val)
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    
for num in range(max_val+1):
    while num in count and count[num] != 0:
        print(num)
        count[num] -= 1