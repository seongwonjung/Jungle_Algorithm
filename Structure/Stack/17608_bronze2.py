# 지금 받는 막대가 더 크다? 앞에 없앤다
import sys
input = sys.stdin.readline
n = int(input().strip())
st = []
for i in range(n):
    h = int(input().strip())
    if not st:
        st.append(h)
        continue
    while (st and st[len(st)-1] <= h):
        st.pop()
    st.append(h)
print(len(st))