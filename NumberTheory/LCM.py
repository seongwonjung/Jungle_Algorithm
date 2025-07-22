# GCD - 최대공약수
def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

# LCM - 최소공배수
# 두 수를 곱한 수에 GCD를 나눈 값과 같다
def lcm(a,b):
    return a*b//gcd(a,b)

print(lcm(14,64))
# 출력 -> 448