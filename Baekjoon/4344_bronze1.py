c = int(input())
for i in range(c):
    inputs = list(map(float, input().split()))
    n = int(inputs[0])
    scores = inputs[1:]
    avg = sum(scores)/n
    avg_upper = 0
    for p in scores:
        if avg < p: avg_upper += 1
    #percent 계산 => (a/n)*100
    print(f"{avg_upper/n*100:.3f}%")