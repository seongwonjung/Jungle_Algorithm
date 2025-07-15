t = int(input())
for i in range(t):
    inputs = input()
    tmp = inputs.split()
    r = int(tmp[0])     # 반복횟수
    s = tmp[1]          # 문자열
    for j in s:
        for k in range(r):  # 문자마다 r번 반복해서 출력
            print(j, end='')
    print()