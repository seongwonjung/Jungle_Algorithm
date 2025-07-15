a = int(input())
b = int(input())
c = int(input())
rst = a*b*c
m = dict()
# dictionary = hashmap임
while (rst > 0):
    num = rst%10
    if not(num in m): m[num] = 1 # 처음 나온 숫자는 키가 정의되지 않아서 1 대입
    else: m[num] += 1 # 이미 나온적 있는 숫자면 +1
    rst = rst//10 # 일의 자릿수 삭제
    
for i in range(10):
    if not(i in m): print(0) # 키가 정의되지 않았다면 한번도 안나온 숫자
    else : print(m[i]) # 정의되어있다면 키의 value 출력