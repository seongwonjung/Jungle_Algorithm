import sys
input = sys.stdin.readline
n = int(input().strip())
A = sorted(list(map(int, input().strip().split())))
# 10 10 20 20 30 50 일 때 음...
# 10 을 선택해 -> 10보다 큰 다음꺼 선택 -> 또 그 다음 큰거 선택 -> 반복
# 이걸 효율적으로 이분탐색으로 찾으면 될 듯 함.
# 우선 첫 비교는 0 번째와 해야 함 0번째 보다 큰 걸 1번째 인덱스에 넣고
# 1번째 인덱스 보다 큰거 2번째에 넣고... 반복
print(A)
rst = [A[0]]
print(rst)