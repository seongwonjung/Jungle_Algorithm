import sys
s = input().strip()
bomb = input().strip()
b_len = len(bomb)
st = []
for i in s:
    st.append(i)
    while(st and "".join(st[len(st)-b_len:]) == bomb):
        for _ in range(b_len):
            st.pop()
            
if st:  print(*st, sep='')
else:   print("FRULA")