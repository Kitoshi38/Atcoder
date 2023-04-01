N, W = map(int, input().split())
vs = []
ws =  []
for i in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if ws[i] <= j:
            dp[i+1][j] = max(dp[i][j], dp[i][j-ws[i]]+vs[i])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])

