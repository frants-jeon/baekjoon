##### 안전 영역 #####
from sys import stdin, setrecursionlimit
import copy
input = stdin.readline
setrecursionlimit(10000)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
answer = []
highest = max(map(max, arr))

def dfs(x, y, rain):
  # 수심보다 더 크면 0으로 만들어 줌
  if arr_tmp[x][y] > rain:
    arr_tmp[x][y] = 0
    # 4 가지 방향 탐색
    if x - 1 >= 0 and arr_tmp[x - 1][y] > rain:
      dfs(x - 1, y, rain)
    if x + 1 < N and arr_tmp[x + 1][y] > rain:
      dfs(x + 1, y, rain)
    if y - 1 >= 0 and arr_tmp[x][y - 1] > rain:
      dfs(x, y - 1, rain)
    if y + 1 < N and arr_tmp[x][y + 1] > rain:
      dfs(x, y + 1, rain)

for r in range(highest + 1):
  cnt = 0
  arr_tmp = copy.deepcopy(arr) # 매번 배열 초기화
  for i in range(N):
    for j in range(N):
      # 수심보다 더 큰 곳의 범위를 0으로 만들고 cnt += 1
      if arr_tmp[i][j] > r:
        dfs(i,j,r)
        cnt += 1
  # 구해진 값을 answer에 넣고 최댓값 출력
  answer.append(cnt)

print(max(answer))