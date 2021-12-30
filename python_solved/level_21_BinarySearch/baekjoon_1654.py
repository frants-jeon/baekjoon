##### 랜선 자르기 #####
from sys import stdin
input = stdin.readline
K, N = map(int,input().split())
lans = [int(input()) for _ in range(K)]
low, high = 0, max(lans) * 2
while low + 1 < high:
  middle = (low + high) // 2
  tmp = 0
  for lan in lans:
    if lan - middle >= 0:
      tmp += lan // middle
  if tmp >= N:
    low = middle
  else: high = middle
print(low)