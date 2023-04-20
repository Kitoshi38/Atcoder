N = int(input())

def divisor_num(n):
    num = 0
    for i in range(1, n+1):
        if n % i == 0:
            num += 1
    return num

ans = 0
for i in range(1, N+1, 2):
    if divisor_num(i) == 8:
        ans += 1

print(ans)
