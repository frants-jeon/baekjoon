##### 뱀 #####
from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
K = int(input())
apples = deque([list(map(int,input().split())) for _ in range(K)])
L = int(input())
directions = deque([list(input().split()) for _ in range(L)]) # 문자임에 주의
# 뱀의 몸이 있는 좌표 덱 생성
snake = deque([[1,1]])
timeCnt = 0
# 뱀의 진행방향 표시 : R,L,U,D로 각각 오,왼,위,아래 표시
moveTo = 'R'

def turnHead(C, d):
  # C = 회전 방향, d = 현재 방향(moveTo)
  if C == 'D':
    if d == 'R': return 'D'
    elif d == 'L': return 'U'
    elif d == 'D': return 'L'
    else: return 'R'
  else:
    if d == 'R': return 'U'
    elif d == 'L': return 'D'
    elif d == 'D': return 'R'
    else: return 'L'

while 1:
  timeCnt += 1
  currentPos = snake[-1]
  if moveTo == 'R':
    nextPos = [currentPos[0],currentPos[1] + 1]
    # 이동할 수 없거나 이미 몸이 있는 자리면 멈춤
    if nextPos[1] >= N + 1 or nextPos in snake: break
    # 이동 가능하니까 뱀 좌표 업데이트
    snake.append(nextPos)
    # 사과가 있으면 사과 삭제. 없으면 꼬리 삭제
    if nextPos in apples:
      apples.remove(nextPos)
    else: snake.popleft()
  # 다른 방향도 위와 같은 매커니즘으로 진행
  elif moveTo == 'L':
    nextPos = [currentPos[0],currentPos[1] - 1]
    if nextPos[1] < 1 or nextPos in snake: break
    snake.append(nextPos)
    if nextPos in apples:
      apples.remove(nextPos)
    else: snake.popleft()
  elif moveTo == 'U':
    nextPos = [currentPos[0] - 1,currentPos[1]]
    if nextPos[0] < 1 or nextPos in snake: break
    snake.append(nextPos)
    if nextPos in apples:
      apples.remove(nextPos)
    else: snake.popleft()
  elif moveTo == 'D':
    nextPos = [currentPos[0] + 1,currentPos[1]]
    if nextPos[0] >= N + 1 or nextPos in snake: break
    snake.append(nextPos)
    if nextPos in apples:
      apples.remove(nextPos)
    else: snake.popleft()
  
  # 방향 변환이 더 남아있고 현재 시각과 맞으면 변환하고 삭제
  if len(directions) != 0:
    if int(directions[0][0]) == timeCnt:
      moveTo = turnHead(directions[0][1],moveTo)
      directions.popleft()
print(timeCnt)