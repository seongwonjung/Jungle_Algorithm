# 슬라이싱으로 뒤집기
s = list(input().split())
a = int(s[0][::-1])
b = int(s[1][::-1])
if a > b : print(a)
else : print(b)

# 반복문으로 뒤집기
# def rev_str(s):
#     rev = ""
#     for i in s:
#         rev = i + rev
#     return rev
# s = list(input().split())
# a = int(rev_str(s[0]))
# b = int(rev_str(s[1]))
# if a > b : print(a)
# else : print(b)

# reversed 함수 이용하기
# s = list(input().split())
# a = int(''.join(reversed(s[0])))
# b = int(''.join(reversed(s[1])))
# if a > b : print(a)
# else : print(b)