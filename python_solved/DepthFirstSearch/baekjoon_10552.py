##### DOM #####
from sys import stdin, setrecursionlimit
from collections import deque
input = stdin.readline
setrecursionlimit(200000)

N, M, channel = map(int,input().split())
ch_info = dict()
# 특정 채널을 싫어하는 사람이 이미 있다면 다음 입력부터는 받지 않기 위해 중복 체크 필요
for _ in range(N):
  tmp = list(map(int,input().split()))
  # a in b의 방식으로 리스트에서 찾으면 시간이 오래 걸려서 dict의 get 이용
  check_overlap = ch_info.get(tmp[1], -1)
  if check_overlap != -1: continue
  ch_info[tmp[1]] = tmp[0]

def dfs(ch):
  global cnt
  # 이미 틀었던 채널이라면 무한히 반복되기 때문에 cnt = -1로 바꿔주고 종료
  if visited[ch]:
    cnt = -1
    return
  # 채널을 싫어하는 사람이 없으면 종료
  if ch_info.get(ch, -1) == -1:
    return
  # 만약 방문을 안했었다면
  if not visited[ch]:
    #방문 여부를 True로 바꾸고 이어서 탐색
    visited[ch] = 1
    cnt += 1
    dfs(ch_info[ch])
    return

cnt = 0
visited = ['0'] + [0] * M
if channel in ch_info.keys():
  dfs(channel)
print(cnt)