W, H = map(int, input().split())

M = 10**9 + 7

def power(x, n):
    if n == 0:
        return 1
    else:
        tmp = power(x*x%M, n//2)
        if n % 2:
            tmp = tmp * x % M
        return tmp

def factorial(x):
    ans = 1
    for i in range(1, x+1):
        ans  = ans * i % M
    return ans

ans = factorial(W+H-2)
s = (factorial(W-1)*factorial(H-1))%M
ans =  ans * power(s, M-2) % M
print(ans) 
