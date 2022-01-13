##### 키로커 #####
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
for _ in range(N):
  password = list(input().strip())
  # 화살표를 누를 때 인덱스가 0이거나 -1 일때 움직이면 안되는 상황 때문에 시작점을 '$'으로 체크
  answer = deque(['$'])
  for key in password:
    # 누른 키가 '<'이면서 시작점이 아닐 때 이동
    # 화살표나 '-'키가 아닌 경우는 모두 append해주기 때문에 and 조건이 아니라 이중 if문 사용
    if key == '<':
      if answer[-1] != '$':
        answer.rotate(1)
    elif key == '>':
      if answer[0] != '$':
        answer.rotate(-1)
    elif key == '-':
      if answer[-1] != '$':
        answer.pop()
    else: answer.append(key)
  # 다시 '$'가 idx 0위치로 오도록 해주고 삭제
  answer.rotate(-answer.index('$'))
  answer.popleft()
  print(''.join(answer))