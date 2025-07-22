# n = 원판의 개수
import sys
print = sys.stdout.write
n = int(input())
routes = []
def hanoi(no, a, b, c):
    global routes
    if(no == 1):
        routes.append([a, c])
    else:
        hanoi(no-1, a, c, b)
        routes.append([a, c])
        hanoi(no-1, b, a, c)

cnt = 2**n - 1   
if(n > 20):
    print("%d\n" %(cnt))
else:
    hanoi(n, 1, 2, 3)
    print("%d\n" %(cnt))
    for a,b in routes:
        print("%d %d\n" %(a, b))