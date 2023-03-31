n = int(input())
q = list(map(int, input().split()))
s = int(input())
T = list(map(int, input().split()))

def bs(arr, num):
    left = 0
    right = len(arr) - 1
    flag = False
    while(left <= right):
        pivot = left+(right-left)//2
        if num == arr[pivot]:
            flag =  True
            break
        elif num < arr[pivot]:
            right = pivot- 1
        else:
            left = pivot + 1

    return flag

ans = 0
for t in T:
    if bs(q, t):
        ans += 1
print(ans)