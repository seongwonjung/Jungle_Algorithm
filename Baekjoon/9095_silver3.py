import sys
input = sys.stdin.readline
numbers = [1,2,3]
t = int(input())
cnt = 0
def perm(n):
    def dfs(total):
        global cnt
        if total > n:
            return
        elif total == n:
            cnt += 1
        for i in range(3):
            dfs(total + numbers[i])
    
    dfs(0)
    print(cnt)
    return 
for i in range(t):
    n = int(input())
    perm(n)
    cnt = 0
