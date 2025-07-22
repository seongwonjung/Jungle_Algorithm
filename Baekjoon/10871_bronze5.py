n, x = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(0, n):
    if numbers[i] < x:
        print(f"{numbers[i]} ", end='')
