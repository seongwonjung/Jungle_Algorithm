import sys
input = sys.stdin.readline
# 1과 00 을 이용해서 n칸을 채운다고 생각하자
# 그럼 1칸 채우기, 2칸 채우기 와 같이 생각할 수 있다.
n = int(input())
def solve(n):
    if n == 1:
        print(1)
        sys.exit(0)
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b, (a+b)%15746
    print(b)
solve(n)