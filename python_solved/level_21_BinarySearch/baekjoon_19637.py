##### IF문 좀 대신 써줘 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
title_list, power_list = [], []
# 칭호와 전투력 상한값 N개 받기
for _ in range(N):
  title, power = input().split()
  if power_list and power_list[-1] == int(power):
    continue
  title_list.append(title)
  power_list.append(int(power))
# 캐릭터 전투력 M개 받기
characters = [int(input()) for _ in range(M)]
# 각 캐릭터마다 전투력 측정
for i in range(M):
  # title 인덱스 기준으로 이분탐색
  low, high = 0, len(power_list) - 1
  while low + 1 < high:
    mid = (low + high) // 2
    # i번째 캐릭터의 전투력이 power의 mid번째 상한값보다 작거나 같으면 high = mid
    if characters[i] <= power_list[mid]: high = mid
    else: low = mid
  # low와 high가 1차이로 while문 종료 후 low값인지 high값인지 판별
  if characters[i] > power_list[low]: print(title_list[high])
  else: print(title_list[low])