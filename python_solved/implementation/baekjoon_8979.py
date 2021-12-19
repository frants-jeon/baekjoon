##### 올림픽 #####
from sys import stdin
input = stdin.readline
N, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
arr.insert(0,[0,0,0,0])
rank = [0]
num = [0]
for i in range(1, N + 1):
  if arr[i][1:] == arr[i - 1][1:]:
    rank.append(rank[i - 1])
    num.append(arr[i][0])
  else:
    rank.append(len(rank))
    num.append(arr[i][0])
print(rank[num.index(K)])
