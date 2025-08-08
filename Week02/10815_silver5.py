# 문제를 보자마자 hash 자료구조(dict, set)를 이용해 풀거나 binary_search를 이용하면 되겠다고 생각함.
import sys
input = sys.stdin.readline
n = int(input().strip())

# 1. set을 이용한 풀이
cards = set(map(int, input().strip().split()))
m = int(input().strip())
target = list(map(int, input().strip().split()))
for i in target:
    if i in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')

# 2. binary_search를 이용한 풀이
cards = (list(map(int, input().strip().split())))
cards.sort()
m = int(input().strip())
target = list(map(int, input().strip().split()))

def find_card(s, e, key):
    while(s <= e):
        mid = (s+e)//2
        if cards[mid] == key:
            return 1
        elif cards[mid] > key:
            e = mid-1
        else:
            s = mid+1
    return 0

for i in target:
    print(find_card(0, n-1, i), end=' ')