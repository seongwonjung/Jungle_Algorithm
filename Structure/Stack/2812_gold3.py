# 문제
# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)
n, k = map(int, input().split())
# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.
number = int(input())
# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
stack = list[]
for i in range(n):
    if len(stack) == 0:     # stack이 비어있다면?
        stack.append(i)
    
# 예제 입력 1 
# 4 2
# 1924
# 예제 출력 1 
# 94