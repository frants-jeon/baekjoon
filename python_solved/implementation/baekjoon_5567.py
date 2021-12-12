##### 결혼식 #####
from sys import int_info, stdin
input = stdin.readline
n, m = int(input()), int(input())
friend = [tuple(map(int,input().split())) for _ in range(m)]
invite = []
for i in range(m):
  if friend[i][0] == 1:
    invite.append(friend[i][1])
  elif friend[i][1] == 1:
    invite.append(friend[i][0])
tmp = []
for j in range(len(invite)):
  for k in range(m):
    if invite[j] == friend[k][0]:
      tmp.append(friend[k][1])
    elif invite[j] == friend[k][1]:
      tmp.append(friend[k][0])
invite = set(invite) | set(tmp)
if 1 in invite:
  invite.remove(1)
print(len(invite))