##### 치킨 배달 #####
from sys import stdin
from itertools import combinations
input = stdin.readline
N, M = map(int,input().split())
town = [list(map(int,input().split())) for _ in range(N)]
house = []
chicken = []
town_chicken_distance = []
for i in range(N):
  for j in range(N):
    if town[i][j] == 1:
      house.append((i,j))
    elif town[i][j] == 2:
      chicken.append((i,j))

arr = list(combinations(chicken, M))
for pick_ckn in arr:
  tmp1 = []
  for i in range(len(house)):
    tmp2 = []
    for j in pick_ckn:
      tmp2.append(abs(house[i][0] - j[0]) + abs(house[i][1] - j[1]))
    tmp1.append(min(tmp2))
  town_chicken_distance.append(sum(tmp1))

print(min(town_chicken_distance))