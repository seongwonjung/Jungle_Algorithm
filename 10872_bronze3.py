n = int(input())
factori = []
# n! = 1*2*3*...*n
for i in range(n+1):
    if i <= 1: factori.append(1)
    else :
        factori.append(factori[i-1]*(i))    # n! = (n-1)!*n

print(factori[n])