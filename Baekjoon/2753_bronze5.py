year = int(input())
# 윤년은 4의 배수 이면서, 100의 배수가 아닐 때 or 400의 배수일 때
if (year%4 == 0)&(year%100!=0): print(1)
elif (year % 400 == 0) : print(1)
else: print(0)