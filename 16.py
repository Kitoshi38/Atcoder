N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

P = list(map(lambda val: val-1, P))
Q = list(map(lambda val: val-1, Q))
ans = 0

intp = int(''.join([f'{num}' for num in P]))
intq = int(''.join([f'{num}' for num in Q]))

if P > Q:
    P, Q = Q, P

def plus(R):
    n = len(R)
    while True:
        for i in range(n-1, -1, -1):
            if R[i] < n-1:
                R[i] += 1
                break
            else:
                R[i] = 0
        if len(set(R)) == n:
            break
    return R

while P != Q:
    P = plus(P)
    ans += 1

print(ans)