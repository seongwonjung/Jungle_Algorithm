import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().strip().split())))
s = 0
e = n-1
rst = []
while(s < e):
    tmp = arr[s] + arr[e]
    rst.append([abs(tmp), s, e])
    if tmp == 0:
        break
    elif tmp < 0:
        s += 1
    else:
        e -= 1

rst = sorted(rst)
print(arr[rst[0][1]], arr[rst[0][2]])