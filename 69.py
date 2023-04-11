Q = int(input())

def is_prime(m):
    if m == 1:
        return False
    flag = True
    for i in range(2, int(m**0.5)+1):
        if m % i == 0:
            flag = False
            break
    return flag

def similar2017(l, r):
    arr2017 = []
    for i in range(l, r+1, 2):
        if is_prime((i+1)//2):
            if is_prime(i):
                arr2017.append(i)
    return arr2017

ls = []; rs = []
for i in range(Q):
    l, r = map(int, input().split())
    ls.append(l); rs.append(r)

l_max = min(ls); r_max = max(rs)
arr2017 = similar2017(l_max, r_max)

def num2017(l, r):
    ans = 0
    for i in range(len(arr2017)):
        if l <= arr2017[i] and arr2017[i] <= r:
            ans += 1
    return ans

for i in range(Q):
    print(num2017(ls[i], rs[i]))
