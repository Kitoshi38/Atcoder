from collections import deque
import sys

def neighbor(w, h):
    land_neighbor = []
    for w_tmp in [w-1, w, w+1]:
        for h_tmp in [h-1, h, h+1]:
            if map_mat[h_tmp][w_tmp]:
                if not (h == h_tmp and w == w_tmp):
                    land_neighbor.append(f'{w_tmp}_{h_tmp}')
    return land_neighbor

def island(W, H, map_mat):
    visited = [[0 for i in range(W+2)] for j in range(H+2)]
    num = 0
    while True:
        # print(visited)
        waiting = deque()
        flag = False
        for h in range(H+2):
            if flag:
                break
            for w in range(W+2):
                if map_mat[h][w] and not visited[h][w]:
                    waiting.append(f'{w}_{h}')
                    flag = True
                    break
     
        if len(waiting):
            num += 1
            while len(waiting):
                cur_node = waiting.pop()
                idx = cur_node.find("_")
                if not visited[int(cur_node[idx+1:])][int(cur_node[:idx])]:
                    visited[int(cur_node[idx+1:])][int(cur_node[:idx])] = 1
                    nei = neighbor(int(cur_node[:idx]), int(cur_node[idx+1:]))
                    # print(nei)
                    if len(nei) != 0:
                        waiting.extend(nei)
        else:
            break
    return num

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        sys.exit()
    else:
        map_mat = [[0 for i in range(W+2)] for j in range(H+2)]
        for i in range(H):
            w = list(map(int, input().split()))
            for j in range(W):
                map_mat[i+1][j+1] = w[j]
        print(island(W, H, map_mat))
            