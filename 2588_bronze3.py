a = int(input())
b = int(input())
# b의 첫째자리 x a => (b%10)*a 
print((b%10)*a)
# b의 둘째자리 x a => (b$100)//10*a
print((b%100)//10*a)
# b의 셋째자리 x a => (b//100)*a
print((b//100)*a)
# a x b =? a*b
print(a*b)