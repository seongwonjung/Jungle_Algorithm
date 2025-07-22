def perm(arr, r):
    used = [False]*len(arr)
    path = []
     
    def dfs():
        if len(path) == r:
            print(path)
            return
        
        for i, v in enumerate(arr):
            if not used[i]:
                used[i] = True  # 1. choose
                path.append(v)
                dfs()           # 2. recurse
                path.pop()
                used[i] = False # 3. un-choose
    dfs()