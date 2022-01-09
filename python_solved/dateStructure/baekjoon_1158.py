##### 요세푸스 문제 #####
from collections import deque
N, k = map(int,input().split())
deq = deque([i for i in range(1, N + 1)])
answer = []
for _ in range(N):
  # 덱을 k번 왼쪽으로 회전하여 인덱스 마지막에 k번째 숫자 위치함.
  deq.rotate(-k)
  # k번째 숫자를 빼서 answer에 추가
  answer.append(deq.pop())
print(f'<{", ".join(map(str,answer))}>')
