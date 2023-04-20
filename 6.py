N = int(input())
S = input()

num = 0
for i in range(1000):
    a = i // 100
    b = (i - a*100) // 10
    c = i - a*100 - b*10

    flag = [False]*3
    for j in range(len(S)):
        if flag[0] and flag[1]:
            if int(S[j]) == c:
                flag[2] = True
                break
        elif flag[0]:
            if int(S[j]) == b:
                flag[1] = True
        else:
            if int(S[j]) == a:
                flag[0] = True

    if flag[2]:
        num += 1
print(num)