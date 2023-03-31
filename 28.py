from collections import deque

n = int(input())
edges_list = []
for i in range(n):
    tmp = list(map(int, input().split()))
    edges_list.append(tmp[2:])

def bfs(edges_list):
    n = len(edges_list)
    d = [0] * n
    flag = [0] * n # 発見済みのはっけんずみのノードを1にする
    flag [0] = 1

    # start
    count = 0
    waiting = deque()
    waiting.append(1)
    repetition = deque()
    repetition.append(1)

    while(len(waiting)):
        rep = 0
        for i in range(repetition.popleft()):
            while(1):
                if not len(waiting):
                    break
                node = waiting.popleft()
                if d[node-1] == 0:
                    cur_node = node
                    break

            if d[cur_node-1] == 0 and cur_node != 1:
                d[cur_node-1] = count
                flag[cur_node-1] = 1
            
            for node in edges_list[cur_node-1]:
                if flag[node-1] == 0 and node != 1:
                    rep += 1
                    flag[node-1] = 1
                    waiting.append(node)
                
        repetition.append(rep)
        count += 1
    
    for i in range(1, len(d)):
        if d[i] == 0:
            d[i] = -1

    return d

d = bfs(edges_list)
for i in range(n):
    print(i+1, d[i])

