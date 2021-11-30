##### 01 타일 #####
from sys import stdin
N = int(stdin.readline())
f1, f2 = 1, 2 
for _ in range(3, N + 1): 
  f1, f2 = f2 % 15746, (f1 + f2) % 15746

if N == 1: print(1)
else: print(f2)