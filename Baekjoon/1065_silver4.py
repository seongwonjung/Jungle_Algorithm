# 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다
# 100 의 자리 이전까지는 모두 한수임

n = int(input())
if(n < 100): print(n)
else:
    cnt = 99 
    for i in range(101, n+1):
        a = i//100
        b = (i%100)//10
        c = i%10
        if (a-b)==(b-c):
            cnt += 1
            
print(cnt)