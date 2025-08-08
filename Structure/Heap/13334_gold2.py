import sys, heapq
input = sys.stdin.readline
n = int(input().strip())
arr = []
heap = []
for _ in range(n):
    h, o = map(int, input().strip().split())
    if h > o:
        h, o = o, h
    arr.append([h, o])
arr.sort(key = lambda x: x[1])
d = int(input().strip())
