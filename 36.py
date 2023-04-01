N, W = map(int, input().split())
vs = []
ws =  []
vws = []
for i in range(N):
    vw = list(map(int, input().split()))
    vws.append(vw)

def chmax(a, b) -> bool:
    if a < b:
        a = b
        return True
    return False
vws.sort(reverse=False, key=lambda x:(x[1], x[0]))
tmp_w = 0
for vw in reversed(vws):
    if vw[1] != tmp_w:
        vs.append(vw[0])
        ws.append(vw[1])
    tmp_w = vw[1]

dp = [0 for _ in range(W+1)]

for i in range(len(vs)):
    for j in range(W+1):
        if j >= ws[i]:
            dp[j] = max(dp[j], dp[j-ws[i]]+vs[i])
# print(dp)
print(dp[W])

