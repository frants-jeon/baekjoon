##### 에디터 #####
from sys import stdin
from collections import deque
input = stdin.readline

sentence = deque(['?'] + list(input().strip()))
N = len(sentence)
M = int(input())
orders = [input().strip() for _ in range(M)] # 물음표를 추가해서 나중에 원상 복귀 시킬 때 참고
for order in orders:
  # 제일 오른쪽에 문자 추가
  if order[0] == 'P':
    sentence.append(order[-1])
  # sentence의 마지막이 '?'면 제일 앞까지 왔다는 뜻이므로 마지막 문자가 '?'가 아닐 때 커서 이동
  elif order == 'L' and sentence[-1] != '?':
    sentence.rotate(1)
  # sentence의 처음이 '?'면 제일 뒤까지 왔다는 뜻이므로 첫 문자가 '?'가 아닐 때 커서 이동
  elif order == 'D' and sentence[0] != '?':
    sentence.rotate(-1)
  # sentence의 처음이 '?'면 제일 앞까지 왔다는 뜻이므로 삭제 불가.
  elif order == 'B' and sentence[-1] != '?':
    sentence.pop()
# 문자를 원상태로 돌려주고 '?'제거 후 프린트
sentence.rotate(-sentence.index('?'))
sentence.popleft()
print(''.join(sentence))
