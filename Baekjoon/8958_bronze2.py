t = int(input())

for i in range(t):
    total_score = 0
    score = 0
    ox = input()
    for ch in ox:
        if ch == 'O': score += 1
        else: score = 0
        total_score += score
    print(total_score)
    