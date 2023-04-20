import collections

n = int(input())
loc = [[0, 0] for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    loc[i][0] = x; loc[i][1] = y

def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

def orthogonal(x, y, x1, y1, x2, y2):
    s = (x1-x)*(x2-x) + (y1-y)*(y2-y)
    if s == 0:
        return True
    else:
        return False

dis_mat = [[0 for i in range(n)] for j in range(n)] 
for i in range(n):
    for j in range(i+1, n):
        d = distance(loc[i][0], loc[i][1], loc[j][0], loc[j][1])
        dis_mat[i][j] = d; dis_mat[j][i] = d

for i in range(n):
    d = dis_mat[i]
