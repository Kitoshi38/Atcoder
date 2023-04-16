N = int(input())
A = list(map(int, input().split()))

sum_A = [0] * (N+1)
for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]

for i in range(N):
    B = [0]*(N-i)
    for j in range(N-i):
        B[j] = sum_A[i+j+1] - sum_A[j]
    print(max(B))