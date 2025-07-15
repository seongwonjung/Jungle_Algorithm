n, r, c = map(int, input().split())
sum = 0
# 사분면 = quadrant
# 기준점 = pivot
def find_z(n, r, c):
    global sum
    if(n < 1): return
    pivot = 2**(n-1)
    area = pivot**2
    quadrant = 1
    if(r < pivot and c < pivot):  quadrant = 1      # 1 사분면
    elif(r < pivot and c >= pivot):   quadrant = 2  # 2 사분면
    elif(r >= pivot and c < pivot):   quadrant = 3  # 3 사분면
    else:   quadrant = 4                            # 4 사분면
    sum += (quadrant-1)*area
    return find_z(n-1, r%pivot, c%pivot)

find_z(n, r, c)
print(sum)