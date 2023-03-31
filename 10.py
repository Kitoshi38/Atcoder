n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

ans_arr = []
for i in range(1 << n):
    num = 0
    for j in range(n):
        if (i >> j) & 1:
            num += A[j]
    ans_arr.append(num)

for i in range(q):
    flag = "no"
    for j in range(len(ans_arr)):
        if m[i] == ans_arr[j]:
            flag = "yes"
            break
    print(flag)