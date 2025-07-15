def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2))+1): # (num**(1/2)) = 제곱근
        if (num % i) == 0: # 다른 수로 나누어 떨어지면 소수가 아님
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for i in numbers:
    if(is_prime(i)): cnt+=1
print(cnt)
