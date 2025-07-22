import sys
input = sys.stdin.readline
n = int(input().strip())
tmp = list(map(int, input().strip().split()))
st = []
rst = []
for idx, h in enumerate(tmp):
    # top = st[-1][1]
    # top의 인덱스 = st[-1][0]
    while(st and st[-1][1] < h):
        st.pop()
        
    if st:
        rst.append(st[-1][0])
    else:
        rst.append(0)
    st.append([idx+1, h])
    
print(*rst)