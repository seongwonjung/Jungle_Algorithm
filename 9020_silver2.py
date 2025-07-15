def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**(1/2))+1): # (num**(1/2)) = 제곱근
        if (num % i) == 0: # 다른 수로 나누어 떨어지면 소수가 아님
            return False
    return True

# 골드바흐 파티션 (소수 + 소수) = 짝수 (적어도 한 개 이상 존재)
# 두 소수의 차이가 가장 작은 것을 출력이니까 num/2 부터 시작해보자

t = int(input())
for i in range(t):
    num = int(input())
    for i in range(num//2, 0, -1):
        if is_prime(i) & is_prime(num-i):
            print(f"{i} {num-i}")
            break
