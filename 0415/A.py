N = int(input())
S = input()

g_flag = False
n_flag = True
for i in range(N):
    if S[i] == "o":
        g_flag = True
    if S[i] == "x":
        n_flag = False

if g_flag and n_flag:
    print("Yes")
else:
    print("No")