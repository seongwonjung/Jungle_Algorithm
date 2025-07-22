def comb_mask(arr, r):
    n = len(arr)
    for mask in range(1 << n):
        if mask.bit_count() == r:
            subset = [arr[i] for i in range(n) if mask & (1 << i)]
            print(subset)
comb_mask(['A','B','C','D'], 2)
print()

def comb(arr, r):
    path = []
    def dfs(start):
        if len(path) == r:
            print(path)
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            dfs(i+1)
            path.pop()
    
    dfs(0)

comb(['A','B','C','D'], 2)