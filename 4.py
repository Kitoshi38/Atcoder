N, M = map(int, input().split())
A = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = a[j]

ans = 0
for i in range(M):
    for j in range(i+1, M):
        ans_tmp = 0
        for k in range(N):
            ans_tmp += max(A[k][i], A[k][j])
        if ans < ans_tmp:
            ans = ans_tmp

print(ans)
