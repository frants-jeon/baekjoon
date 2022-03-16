##### 용돈 관리 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
days = [int(input()) for _ in range(N)]
low, high = 0, 1000000000
while low + 1 < high:
  middle = (low + high) // 2 # 인출한 돈
  current_money = middle # 현재 잔액
  cnt = 1 # 인출 횟수
  sizeDown = 1 # high값을 낮춰야 하는지 여부
  for i in range(N):
    # i번째 날에 써야할 돈이 출금한 금액보다 많다면 break하고 출금액을 높임
    if days[i] > middle:
      sizeDown = 0
      break
    # 오늘 쓸 금액이 충분하다면 현재 잔액에서 빼줌
    elif current_money - days[i] >= 0:
      current_money -= days[i]
    else: # 추가로 출금해야 한다면 인출횟수 늘리고 현재잔액 갱신
      current_money = middle - days[i]
      cnt += 1
  # 사이즈 줄여야하지 않거나 인출횟수가 초과했다면 low값 갱신(인출금액 상향)
  if sizeDown == 0 or cnt > M:
    low = middle
  else: # 그 외의 경우는 high값 갱신(인출금액 하향)
    high = middle

print(high)