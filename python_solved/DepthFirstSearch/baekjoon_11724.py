##### 연결 요소의 개수 #####
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
# 시간초과 해결을 위해 u에서 v로, v에서 u로 가는 간선을 오름차순으로 따로 만들어줌
sorted_UtoV = sorted(arr, key=lambda x: x[0])
sorted_VtoU = sorted(arr, key=lambda x: x[1])
UtoV_from = list(map(lambda x: x[0], sorted_UtoV))
UtoV_to = list(map(lambda x: x[1], sorted_UtoV))
VtoU_from = list(map(lambda x: x[1], sorted_VtoU))
VtoU_to = list(map(lambda x: x[0], sorted_VtoU))


def dfs(idx):
  global cnt
  # 이미 방문이 완전히 끝났으면 그냥 종료
  if visited[idx]: return
  # 탐색 시 시간을 줄이기 위해 시작점 생성
  VtoU_start = M
  UtoV_start = M
  if idx in VtoU_from:
    VtoU_start = VtoU_from.index(idx)
  if idx in UtoV_from:
    UtoV_start = UtoV_from.index(idx)
  # idx에서 이어진 간선이 없으면 종료
  elif idx not in VtoU_from:
    visited[idx] = 1
    return
  # 방문한 적이 없는 경우 dfs 시작
  if not visited[idx]:
    visited[idx] = 1
    # u에서 v로 가는 간선 탐색
    for i in range(UtoV_start, M):
      if UtoV_from[i] > idx: break
      if UtoV_from[i] == idx:
        dfs(UtoV_to[i])
    # v에서 u로 가는 간선 탐색
    for i in range(VtoU_start, M):
      if VtoU_from[i] > idx: break
      if VtoU_from[i] == idx:
        dfs(VtoU_to[i])
    return


cnt = 0
visited = ['0'] + [0] * N
for i in range(1, N + 1):
  if not visited[i]:
    dfs(i)
    cnt += 1
print(cnt)