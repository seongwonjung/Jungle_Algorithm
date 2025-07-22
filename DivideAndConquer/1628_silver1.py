import sys
input = sys.stdin.readline
a, b, c = map(int, input().strip().split())
# a^b = a^(b//2)*a^(b//2)
# (a*b)%c = (a%c)*(b%c)%c
def square(a, b):
    if b == 1:
        return a % c
    tmp = square(a, b//2)
    if b % 2 == 0:
        return (tmp*tmp)%c
    else:
        return (tmp*tmp*a)%c
a = square(a,b)
print(a%c)