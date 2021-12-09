##### 방 번호 #####
from sys import stdin
N = stdin.readline()
cnt_list = [0 for i in range(10)]
for i in range(10):
  cnt = N.count(f'{i}')
  if i == 6 or i == 9:
    cnt_list[9] += cnt
  else: cnt_list[i] += cnt

cnt_list[9] = (cnt_list[9] + 1) // 2
print(max(cnt_list))