##### 덱 #####
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
orders = [input().strip() for _ in range(N)]
que = deque()
for order in orders:
  if order == 'pop_front':
    if que: print(que.popleft())
    else: print(-1)
  elif order == 'pop_back':
    if que: print(que.pop())
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
  else:
    push, num = order.split()
    if push == 'push_front':
      que.appendleft(num)
    else: que.append(num)
