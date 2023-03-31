import math
import itertools
import numpy as np

N = int(input())
positions = []
for i in range(N):
    x_tmp, y_tmp = map(int, input().split())
    positions.append([x_tmp, y_tmp])

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def all_distance(posi_arr):
    output = 0
    for i in range(len(posi_arr)-1):
        output += distance(posi_arr[i][0], posi_arr[i][1], posi_arr[i+1][0], posi_arr[i+1][1])
    return output

length_arr = []
for position in list(itertools.permutations(positions, N)):
    length_arr.append(all_distance(position))
print(np.average(length_arr))
