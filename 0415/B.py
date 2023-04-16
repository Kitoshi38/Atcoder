N = int(input())
A = [[0 for i in range(N)] for j in range(N)]
B = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    a_row = list(map(int, input().split()))
    for j in range(N):
        A[i][j] = a_row[j]

for i in range(N):
    b_row = list(map(int, input().split()))
    for j in range(N):
        B[i][j] = b_row[j]

def rot(A):
    rot_A = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            rot_A[i][j] = A[N-1-j][i]
    return rot_A

def same(A, B):
    flag = True
    for i in range(N):
        if flag:
            for j in range(N):
                if A[i][j]:
                    if B[i][j] == 0:
                        flag = False
                        break
    return flag

flag = False
for i in range(N):
    if same(A, B):
        flag = True
        break
    else:
        A = rot(A)

if flag:
    print("Yes")
else:
    print("No")