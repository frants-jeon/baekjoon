##### 팩토리얼 0의 갯수 #####
from sys import stdin
def f(n):
  if n == 1 or n == 0:
    return 1
  return n * f(n - 1)
num_str = str(f(int(stdin.readline())))
cnt = 0
for i in range(len(num_str) - 1, -1, -1):
  if num_str[i] == '0':
    cnt += 1
  else: break
print(cnt)