##### AC #####
from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for _ in range(T):
  P = input().strip()
  n = int(input())
  arr = deque()
  tmp = ''
  # 배열을 받아서 돌면서 숫자면 tmp에 추가했다가 숫자로 변환해서 arr에 추가
  for num in input().strip():
    if num.isdigit():
      tmp += num
    elif tmp != '':
      arr.append(int(tmp))
      tmp = ''

  isFront = True
  for p in P:
    # 함수가 R일때 isFront가 False면 True로, True면 False로 바꿔줌
    if p == 'R':
      isFront = not isFront
    # 함수가 R이 아니고(D이고) arr가 비어있지 않고 isFront가 True면 앞에서 pop
    elif isFront and arr:
      arr.popleft()
    # 함수가 R이 아니고(D이고) arr가 비어있지 않고 isFront가 False면 뒤에서 pop
    elif not isFront and arr:
      arr.pop()
    else:
      arr = 'error'
      break
  
  if arr == 'error':
    print('error')
  else:
    # isFront가 False면 뒤집어주기
    if not isFront:
      arr.reverse()
    # 띄워쓰기 없이 출력
    print('[', end='')
    arrLen = len(arr)
    for i in range(arrLen):
      if i != arrLen - 1:
        print(arr[i], end=',')
      else: print(arr[i], end='')
    print(']')