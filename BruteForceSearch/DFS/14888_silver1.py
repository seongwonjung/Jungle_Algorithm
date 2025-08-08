# import sys, math
# input = sys.stdin.readline
# # 숫자의 개수
# n = int(input())
# A = list(map(int, input().strip().split()))
# min_val = math.inf
# max_val = -math.inf
# def dfs(x, tmp, operator):
#     # operator 기준으로 돌자
#     # x는 1부터 시작 하니까 A[0] op A[1] 를 tmp 에 넣으면서 min_sum, max_sum 을 구하면 될 듯?
#     # tmp = tmp(애를 처음에 A[0]으로 넣고) op A[x]
#     global min_val, max_val
#     if x == n:
#         if min_val > tmp:
#             min_val = tmp
#         if max_val < tmp:   
#             max_val = tmp
#         return
#     for i in range(4):
#         if operator[i] != 0:
#             if i == 0:      # 덧셈
#                 next_val = tmp + A[x]
#             elif i == 1:    # 뺄셈
#                 next_val = tmp - A[x]
#             elif i == 2:    # 곱셈
#                 next_val = tmp * A[x]
#             else:           # 나눗셈 음수일 때는 양수로 바꾸 뒤 몫을 구한 뒤 -몫
#                 if tmp < 0:
#                     next_val = (abs(tmp) // A[x])*-1
#                 else:
#                     next_val = tmp // A[x]
#             operator[i] -= 1
#             dfs(x+1, next_val, operator)
#             operator[i] += 1
        

# # 덧셈, 뺄셈, 곱셈, 나눗셈 (총 n-1 개)
# operator = list(map(int, input().strip().split()))
# # A0, A1, A2, ... 사이에 연산자들을 어떻게 넣느냐
# dfs(1, A[0], operator)
# print(max_val)
# print(min_val)

import sys
input = sys.stdin.readline
# N = 숫자 개수
N = int(input())
# A = 숫자 배열
A = list(map(int, input().split()))
# A0 op A1 op A2 ... 
INF = sys.maxsize
min_val = INF
max_val = -INF
def dfs(x, tmp, op):
    global min_val, max_val
    if x == N:
        min_val = min(tmp, min_val)
        max_val = max(tmp, max_val)
        return
        
    for i in range(4):
        if op[i] > 0:    
            if i == 0:      # 덧셈
                next_val = tmp + A[x]
            elif i == 1:    # 뺄셈
                next_val = tmp - A[x]
            elif i == 2:    # 곱셈
                next_val = tmp * A[x]
            else:           # 나눗셈
                if tmp < 0:
                    next_val = -tmp // A[x]
                    next_val = -next_val
                else:   next_val = tmp // A[x]
            op[i] -= 1
            dfs(x+1, next_val, op)
            op[i] += 1
    
# 연산자 개수 = N-1
# 덧셈, 뺄셈, 곱셈, 나눗셈 순
op = list(map(int, input().split()))
dfs(1, A[0], op)
print(max_val)
print(min_val)