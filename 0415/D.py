Q = int(input())
M = 998244353
ans = 1
def change(query, ans):
    if query[0] == 1:
        x = query[1]
        ans = 10 * ans + x
        print("0", ans)
    elif query[0] == 2:
        ans = ans // 10
        print("1", ans)
    else:
        print(ans%M)
    return ans

for i in range(Q):
    query = list(map(int, input().split()))
    ans = change(query, ans)