from collections import deque

n = int(input())
edges_list = []
for i in range(n):
    tmp = list(map(int, input().split()))
    edges_list.append(tmp[2:])

def dfs(edges_list):
    n = len(edges_list)
    d = [0] * n
    f = [0 for _ in range(n)]
    rec = []

    # start
    count = 0
    # rec.append(1)
    d[0] = count
    waiting = deque()
    
    s = 2
    start_node = [1]
    while(s <= n):
        flag = False
        for i in range(n):
            if not flag:
                for node in edges_list[i]:
                    if s == node:
                        flag = True
                        break
            else:
                break
        if not flag:
            start_node.append(s)
        s += 1
    
    for start in reversed(start_node):
        waiting.append(start)

    while(len(waiting)):
        cur_node = waiting.pop()
        rec.append(cur_node)
        if d[cur_node-1] == 0:
            count += 1
            d[cur_node-1] = count
            for node in reversed(rec):
                f_flag = True
                for n in edges_list[node-1]:
                    # if (n != node and f[n-1] == 0) or :
                    if d[n-1] == 0:
                        f_flag = False
                        break

                if f_flag and f[node-1] == 0:
                    count += 1
                    f[node-1] = count
                elif not f_flag:
                    break
        
            for node in reversed(edges_list[cur_node-1]):
                if d[node-1] == 0:
                    waiting.append(node)
    return d, f

d, f = dfs(edges_list)
for i in range(n):
    print(i+1, d[i], f[i])

