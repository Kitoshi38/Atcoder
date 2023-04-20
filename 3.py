S = input()

num_arr = []
num = 0
for i in range(len(S)):
    if S[i] == "A" or S[i] == "T" or S[i] == "G" or S[i] == "C":
        num += 1
        if i == len(S)-1:
            num_arr.append(num)
    else:
        if num:
            num_arr.append(num)
        num = 0
if len(num_arr):
    ans = max(num_arr)
else:
    ans = 0
print(ans)
        