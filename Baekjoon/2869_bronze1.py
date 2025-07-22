a, b, v = map(int, input().split())
# a만큼 올라감 b 만큼 내려감 v = 높이
# 하루에 올라가는 높이 = (a-b)
# day = (a-b)/v 
# 단, 정상에 도달할때는 미끄러지지 않음.(+a 이후 -b 를 하지 않음)
# 따라서 (v-b) 높이만큼 (a-b) 만큼씩 올라감
day = (v-b)//(a-b)
# 남은 거리가 있다면 +1
if day*(a-b) < (v-b) : day += 1
print(day)