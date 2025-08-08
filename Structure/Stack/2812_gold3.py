import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())
numbers = input().strip()
rst = [int(numbers[0])]

cnt = 0
for i in range(1, n):
    num = int(numbers[i])
    if not rst:
        rst.append(num)
        continue
    
    if rst[-1] < num:
        while(rst and k > cnt and rst[-1] < num):
            rst.pop()
            cnt += 1
        rst.append(num)
    else:
        rst.append(num)
        
# 처음에 틀림 남은 k가 있어서
# 반복이 끝난 뒤, cnt(사용한 제거 수)가 k보다 작으면
if cnt < k:
    rst = rst[:-(k - cnt)]   # 뒤에서 (k-cnt)개 더 제거
print(*rst, sep='')