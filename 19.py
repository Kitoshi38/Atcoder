d = int(input())
n = int(input())
m = int(input())

store = [0] * (n+1)
delivery = [0] * m


for i in range(n-1):
    s = int(input())
    store[i+1] = s
store[n] = d
store = sorted(store)

for i in range(m):
    deliv = int(input())
    delivery[i] = deliv

# print(store, delivery)
def NearestStore(deli):
    left = 0
    right = n
    while left < right:
        pivot = (left+right) // 2
        if store[pivot] < deli:
            left = pivot + 1
        else:
            right = pivot
    nearest = min(abs(store[pivot-1]-deli), abs(store[pivot]-deli), abs(store[pivot+1]-deli))
    return nearest

ans = 0
for i in range(m):
    ans += NearestStore(delivery[i])

print(ans)

        