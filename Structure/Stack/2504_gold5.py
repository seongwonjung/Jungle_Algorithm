import sys
input = sys.stdin.readline
arr = input().strip()
st = []
# isinstance
for pos in arr:
    if pos == '(' or pos == '[':
        st.append(pos)
    elif pos == ')' or pos == ']':
        if not st:
            print(0)
            exit()
        tmp = 0
        while st:
            top = st.pop()
            if isinstance(top, int):
                tmp += top
            elif top == '(' and pos == ')':
                st.append(2 if tmp == 0 else tmp*2)
                break
            elif top == '[' and pos == ']':
                st.append(3 if tmp == 0 else tmp*3)
                break
            else:   # 괄호쌍이 안맞는 경우
                print(0)
                exit()
        else:   # 여는 괄호가 안나온 경우
            print(0)
            exit()
    else:
        print(0)
        exit()

for a in st:
    if not isinstance(a, int):
        print(0)
        exit()

print(sum(st))