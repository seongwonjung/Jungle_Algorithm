w, h = map(int, input().split())
t = int(input())
cut_x = [False]*w
cut_y = [False]*h
for i in range(t):
    a, b = map(int, input().split())
    if(a == 0): cut_y[b] = True # 가로 자르기
    else: cut_x[b] = True # 세로 자르기
def slice_paper(cut):
    pre = 0
    max_len = 0
    length = len(cut)
    for i in range(length):
        if(cut[i]):
            l = i-pre
            if(max_len < l): max_len = l
            pre = i
        if(i == length-1):
            if(max_len < length-pre): max_len = length-pre
    return max_len

len_x = slice_paper(cut_x)
len_y = slice_paper(cut_y)
print(len_x*len_y)