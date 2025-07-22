def sieve(n):
    is_prime = [False][False] + [True]*(n-1)    # 0,1 제외
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for k in range(p*p, n+1, p):
                is_prime[k] = False
    return [i for i, prime in enumerate(is_prime) if prime]

#  **p × p부터 지우는 이유**  
#  p·2, p·3, …, p·(p−1) 은 이미 (2·p, 3·p, …, (p−1)·p) 로 더 작은 소수 단계에서 지워졌기 때문입니다.  
#   → 조건식을 `k = p*p` 로 시작하면 중복 계산이 확 줄어듭니다.