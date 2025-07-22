# GCD - 최대공약수
def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

a = 270
b = 192
print(gcd(a,b))