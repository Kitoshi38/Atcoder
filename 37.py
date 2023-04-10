n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [n+1] * (n+1)

for i in range(1,n+1):
    for j in range(m):
        if i == c[j]:
            dp[i] = 1
        if i > c[j] and dp[i-c[j]]:
            if dp[i] == 0:
                dp[i] += 1
            else:
                dp[i] = min(dp[i], dp[i-c[j]]+1)

print(dp[n])