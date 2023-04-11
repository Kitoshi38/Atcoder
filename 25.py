from collections import deque

W, H = map(int, input().split())

def neighbor(w, h, map_mat):
    if w 
def island(W, H, map_mat):
    def neighbor(w, h):
        if w-1 >
    islands = []
    for h in range(H):
        for w in range(W):
            if map_mat[h][w]:
                islands.append([f'{w}{h}'])

    if len(islands) == 0:
        return 0
    
    visited = [[0 for i in range(W)] for j in range(H)]
    waiting = deque()
    while len(waiting):
        cur_node = waiting.pop()