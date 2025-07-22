x, y, w, h = map(int, input().split())
# (x,y)는 점의 좌표, (w,h)는 직사각형의 오른쪽 꼭짓점
# up = h-y    down = y    right = w-x     left = x
routes = [h-y, y, w-x, x]
# 이 중 가장 짧은 경로
shortest = min(routes)
print(shortest)