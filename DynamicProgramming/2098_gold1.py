import sys
input = sys.stdin.readline
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*(1<<n) for _ in range(n)]

def TSP(cur, vst):
    # 탈출조건 -> 모든 도시를 방문 했을 경우
    if vst == (1<<n)-1:
        # 모든 도시 방문 후 0번 도시로 돌아가는 경우를 더해주며 리턴
        return W[cur][0] if W[cur][0] != 0 else float('inf')
    
    # 메모이제이션
    if dp[cur][vst] != -1:
        # 처리된 적 있다면 바로 리턴
        return dp[cur][vst]
    
    cost = float('inf')
    
    for nxt in range(n):    # 도시 n만큼 순회
        # 이미 방문 했는지, nxt로 갈 수 있는지
        if not vst&(1<<nxt) and W[cur][nxt] != 0:
            new_cost = TSP(nxt, vst|(1<<nxt)) + W[cur][nxt]
            cost = min(cost, new_cost)

    dp[cur][vst] = cost
    return cost

print(TSP(0, 1))