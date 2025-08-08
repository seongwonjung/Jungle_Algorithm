import sys
input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split()))for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 0
end = -1
for s, e in meetings:
    if s >= end:
        end = e
        cnt += 1
print(cnt)