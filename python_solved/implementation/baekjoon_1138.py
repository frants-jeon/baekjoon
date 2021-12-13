##### 한 줄로 서기 #####
from sys import stdin
input = stdin.readline
N = int(input())
line = list(enumerate(map(int,input().split())))
while 1:
  check = 0
  for i in range(N):
    cnt = 0
    for j in range(i):
      if line[i][0] < line[j][0]:
        cnt += 1
    if line[i][1] < cnt:
      line.insert(i - 1,line.pop(i))
      check += 1
    elif line[i][1] > cnt:
      line.insert(i + 1, line.pop(i))
      check += 1
  if check == 0: break

for k in range(N):
  print(line[k][0] + 1, end=' ')
print()