A, B, C, X, Y = map(int, input().split())
max_c = 2 * max(X, Y)
value = 10**9
for c_num in range(0, max_c+1, 2):
    a_num = max(0, X - c_num//2)
    b_num = max(0, Y - c_num//2)
    tmp = a_num * A + b_num * B + c_num * C
    if tmp <= value:
        value = tmp
print(value)
