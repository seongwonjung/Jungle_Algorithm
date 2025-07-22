import sys
input = sys.stdin.readline

people = [int(input()) for _ in range(9)]
rst = []
vst = [False]*9
def dfs(depth, start, curr_sum, path):
    if depth == 7: # 7명 선택 했을때 return
        if curr_sum == 100: # 난쟁이들 키 합이 100일 경우 rst 넣기
            rst.extend(sorted(path))
        return
    for i in range(start, 9):
        if not vst[i]:
            vst[i] = True
            # start = 현재 선택한 난쟁이+1 로 재귀
            dfs(depth+1, start+1, curr_sum+people[i], path+[people[i]])
            vst[i] = False
            if not(rst == []):
                return

dfs(0,0,0,[])
for i in rst:
    print(i)