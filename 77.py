n, m = map(int, input().split())
M = 10**5
d_sum = [0] * n
for i in range(n-1):
    d_tmp = int(input())
    d_sum[i+1] = d_sum[i] + d_tmp

all_distance = 0
cur_node = 0
for i in range(m):
    b_tmp = int(input())
    all_distance += (abs(d_sum[cur_node] - d_sum[cur_node+b_tmp]) % M)
    cur_node += b_tmp

print(all_distance % M)