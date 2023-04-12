from collections import deque

d = deque(['12', '34', '56'])
while len(d):
    print(d.pop())