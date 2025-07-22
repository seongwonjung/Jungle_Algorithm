def is_prime(n: int) -> bool:
    if n <= 1:      # 0, 1, 음수는 소수가 아님
        return False
    if n % 2 == 0:  # 짝수는 소수가 아님
        return False
    for d in range(3, int(n**0.5)+1, +2):   # 홀수만 검사
        if n % d == 0:
            return False
    return True