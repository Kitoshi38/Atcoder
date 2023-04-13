from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [[0 for i in range(C)] for j in range(R)]
route = [[-1 for i in range(C)] for j in range(R)]
for i in range(R):
    c = input()
    for j in range(C):
        if c[j] == ".":
            maze[i][j] = 1

def neighbor(y, x):
    n_arr = []
    y_n = [y, y, y-1, y+1]
    x_n = [x-1, x+1, x, x]
    for y_tmp, x_tmp in zip(y_n, x_n):
        if maze[y_tmp][x_tmp] and route[y_tmp][x_tmp] < 0:
            n_arr.append(f'{y_tmp}_{x_tmp}')
    return n_arr

def bfs(maze, sy, sx, gy, gx):
    waiting = deque()
    waiting.append(f'{sy}_{sx}')
    route[sy][sx] = 0
    while(len(waiting)):
        if route[gy][gx] >= 0:
            return route[gy][gx]
        cur_node = waiting.popleft()
        idx = cur_node.find('_')
        cur_y = int(cur_node[:idx]); cur_x = int(cur_node[idx+1:])
        n_arr = neighbor(cur_y, cur_x)
        for i in range(len(n_arr)):
            r = route[cur_y][cur_x]
            idx = n_arr[i].find('_')
            next_y = int(n_arr[i][:idx]); next_x = int(n_arr[i][idx+1:])
            if route[next_y][next_x] < 0:
                route[next_y][next_x] = r + 1
        waiting.extend(n_arr)

print(bfs(maze, sy-1, sx-1, gy-1, gx-1))
