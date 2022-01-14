##### 행운의 바퀴 #####
from sys import stdin
input = stdin.readline

N, K = map(int,input().split())
S, A, answer = [], [], ['?'] * N # S는 돌아간 횟수, A는 적혀있는 alphabet
for _ in range(K):
  tmp = input().strip()
  S.append(int(tmp[0]))
  A.append(tmp[-1])
answer[0] = A[-1] #제일 마지막 문자부터 출력하니까 마지막 문자 저장.
# 현재 위치와 이동할 횟수
currentIdx, move = 0, S[-1]
for i in range(K - 2, -1, -1):
  # 새 문자 위치 지정
  newIdx = (currentIdx + move) % N
  # 해당 위치에 문자가 없으면 문자 넣어주고 위치와 이동횟수 재설정
  if answer[newIdx] == '?' and A[i] not in answer:
    answer[newIdx] = A[i]
    currentIdx, move = newIdx, S[i]
  # 이미 문자가 들어와 있는데 다른 문자를 넣으려고 하면 '!' 출력
  elif answer[newIdx] != A[i]:
    answer = '!'
    break
  # 이미 같은 문자가 들어와있으면 위치와 횟수 재설정만 진행
  else: currentIdx, move = newIdx, S[i]
print(''.join(answer))
