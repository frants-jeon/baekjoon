##### 카드2 #####
from sys import stdin
from collections import deque
N = int(stdin.readline())
deq = deque(list(range(1, N + 1)))
while len(deq) > 1:
  deq.popleft()
  deq.rotate(-1)
print(deq[0])