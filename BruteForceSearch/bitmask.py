def subsets_bitmask(items):
    n = len(items)
    for mask in range(1 << n):  # 0 ~ (2^n)-1
        subset = [items[i] 
                  for i in range(n) if mask & (1 << i)]
        print(f"{mask:0{n}b} -> {subset}")

subsets_bitmask(['A','B','C'])