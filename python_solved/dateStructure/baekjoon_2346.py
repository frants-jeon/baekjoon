##### 풍선 터뜨리기 #####
from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
move_deq = deque(list(map(int,input().split())))
balloons_deq = deque(list(range(1, N + 1)))
answer = []

for _ in range(N):
  # 제일 왼쪽 풍선과 종이(move)를 빼서 풍선 번호는 정답에 추가
  move = move_deq.popleft()
  answer.append(balloons_deq.popleft())
  # move가 음수면 그대로 움직임
  if move < 0:
    move_deq.rotate(-move)
    balloons_deq.rotate(-move)
  # move가 양수인 경우에는 move를 이미 하나 뺐기 때문에 1 - move만큼 움직임
  else:
    move_deq.rotate(1 - move)
    balloons_deq.rotate(1 - move)
print(' '.join([str(i) for i in answer]))