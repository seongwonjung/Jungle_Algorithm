idx = 0
max_num = 0
for i in range(9):
    num = int(input())
    if max_num < num: 
        max_num = num
        idx = int(i)
print(max_num)
print(i)