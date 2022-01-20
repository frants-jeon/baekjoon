##### 큐 #####
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
orders = [input().strip() for _ in range(N)]
que = deque()
for order in orders:
  if order == 'pop':
    if que: print(que.popleft())
    else: print(-1)
  elif order == 'size':
    print(len(que))
  elif order == 'empty':
    if que: print(0)
    else: print(1)
  elif order == 'front':
    if que: print(que[0])
    else: print(-1)
  elif order == 'back':
    if que: print(que[-1])
    else: print(-1)
  else: que.append(order[5:])