##### 수 찾기 #####
from sys import stdin
input = stdin.readline
N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
B = list(map(int,input().split()))

for i in range(M):
  arr = A
  low, high = 0, N
  center_idx = (low + high) // 2
  while low + 1 < high:
    if B[i] < arr[center_idx]:
      high = center_idx
    else: low = center_idx
    center_idx = (low + high) // 2
  if B[i] == arr[low]: print(1)
  else: print(0)
