n, c = map(int, input().split())
house = sorted(list(int(input()) for _ in range(n)))
start = house[0]
end = house[-1] - start
rst = 0
while(start <= end):
    mid = (start+end)//2
    count = 1
    last = house[0]
    for i in range(1, n):
        if house[i] - last >= mid:
            last = house[i]
            count += 1
    if(count >= c):
        rst = mid
        start = mid+1
    else:
        end = mid-1
    
print(rst)