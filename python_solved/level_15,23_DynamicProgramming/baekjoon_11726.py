##### 2xn 타일링 #####
from sys import stdin
n = int(stdin.readline())
f1, f2 = 1, 2
for i in range(3, n + 1):
  f1, f2 = f2 % 10007, (f1 + f2) % 10007

if n == 1: print(1)
else: print(f2)
