n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(m):
    