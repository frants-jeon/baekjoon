##### 드래곤 앤 던전 #####
from sys import stdin
input = stdin.readline
N, atk = map(int,input().split())
rooms = [list(map(int,input().split())) for _ in range(N)]
low, high = 0, pow(1000000, 2) * 123456
while low + 1 < high:
  current_atk = atk
  middle = (low + high) // 2
  current_hp = middle
  life = 1
  for room in rooms:
    if room[0] == 1:
      if room[2] % current_atk > 0:
        atk_cnt = room[2] // current_atk
      else: atk_cnt = room[2] // current_atk - 1
      if atk_cnt * room[1] >= current_hp:
        life = 0
        break
      else: current_hp -= atk_cnt * room[1]
    elif room[0] == 2:
      if current_hp + room[2] >= middle:
        current_hp = middle
      else: current_hp += room[2]
      current_atk += room[1]
  if life == 0: low = middle
  else: high = middle
print(high)