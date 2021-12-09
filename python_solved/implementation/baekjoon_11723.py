##### 집합 #####
from sys import stdin
input = stdin.readline
M = int(input())
S = set()
for _ in range(M):
  tmp = list(map(str,input().split()))
  if len(tmp) != 1:
    tmp[1] = int(tmp[1])
  if tmp[0] == 'add':
    S.add(tmp[1])
  elif tmp[0] == 'remove':
    if tmp[1] in S:
      S.remove(tmp[1])
  elif tmp[0] == 'check':
    if tmp[1] in S: print(1)
    else: print(0)
  elif tmp[0] == 'toggle':
    if tmp[1] in S:
      S.remove(tmp[1])
    else: S.add(tmp[1])
  elif tmp[0] == 'all':
    S = {i for i in range(1, 21)}
  else: S.clear()
