import sys
input = sys.stdin.readline
expr = input().strip().split('-')
rst = sum(map(int, expr[0].split('+')))
for i in range(1, len(expr)):
    rst -= sum(map(int, expr[i].split('+')))
print(rst)
# import sys, re
# input = sys.stdin.readline
# # - 가 나오면 ()친다.
# # - 가 나오고 다음 - 나오기 전까지
# expr = input().strip()
# # 숫자 추출
# nums = list(map(int, re.split(r'[+-]', expr)))
# # 연산자 추출
# ops = re.findall(r'[+-]', expr)
# rst = nums[0]
# i = 0
# while i < len(ops):
#     if ops[i] == '+':
#         rst += nums[i+1]
#         i += 1
#     else:
#         tmp = nums[i+1]
#         j = i + 1
#         # 다음 '-' 나오기 전까지 모두 더한 뒤 한꺼번에 빼기
#         while j < len(ops) and ops[j] == '+':
#             tmp += nums[j+1]
#             j += 1
#         rst -= tmp
#         i = j
# print(rst)