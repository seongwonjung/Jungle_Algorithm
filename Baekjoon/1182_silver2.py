import sys
input = sys.stdin.readline
n, s = map(int, input().split())
items = list(map(int, input().split()))
def bit_mask(items, cnt = 0):
    n = len(items)
    for mask in range(1 << n):
        subsets = [items[i] for i in range(n) if mask & (1 << i)]
        if subsets != [] and sum(subsets) == s:
            cnt += 1
    return cnt

print(bit_mask(items))