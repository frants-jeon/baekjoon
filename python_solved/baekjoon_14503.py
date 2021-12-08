##### 로봇청소기 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
robot = list(map(int,input().split()))
room = []
for _ in range(N):
  room.append(list(map(int,input().split())))
r, c, d = robot[0], robot[1], robot[2]
cnt = 1

def move(_d):
  global r, c, d
  if room[r - 1][c] != 0 and room[r + 1][c] != 0 and room[r][c + 1] != 0 and room[r][c - 1] != 0:
    if d == 0:
      if r + 1== N - 1 or room[r + 1][c] == 1: return False
      else: r += 1
      return move(_d)
    elif d == 1:
      if c - 1== 0 or room[r][c - 1] == 1: return False
      else: c -= 1
      return move(_d)
    elif d == 2:
      if r - 1 == 0 or room[r - 1][c] == 1: return False
      else: r -= 1
      return move(_d)
    elif d == 3:
      if c + 1 == M - 1 or room[r][c + 1] == 1: return False
      else: c += 1
      return move(_d)
  else:
    if _d == 0:
      if room[r][c - 1] == 0:
        c, d = c - 1, 3
        return 
      else: return move(3)
    if _d == 1:
      if room[r - 1][c] == 0:
        r, d = r - 1, 0
        return
      else: return move(0)
    if _d == 2:
      if room[r][c + 1] == 0:
        c, d = c + 1, 1
        return
      else: return move(1)
    if _d == 3:
      if room[r + 1][c] == 0:
        r, d = r + 1, 2
        return
      else: return move(2)


def robot_cleaning():
  global cnt,r,c,d
  if room[r][c] == 0:
    cnt += 1
    room[r][c] = cnt
  if move(d) == False: return cnt
  return robot_cleaning()

print(robot_cleaning() - 1)