N, W = map(int, input().split())
vs = []
ws =  []
for i in range(N):
    v, w = map(int, input().split())
    vs.append(v)
    ws.append(w)
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W):
        if dp[i][j] + w[i] <= W:
