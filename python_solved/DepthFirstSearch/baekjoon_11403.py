##### 경로 찾기 #####
from sys import stdin, setrecursionlimit
setrecursionlimit(20000)
input = stdin.readline

N = int(input())
# 2차원 배열 i에서 j까지의 간선이 있는지 여부를 나타내는 arr
arr = [list(map(int,input().split())) for _ in range(N)]

def dfs(idx):
  # idx는 arr에서 i를 나타냄. 행마다 visited를 초기화 해주므로 visited[j]를 방문하지 않았고 arr[i][j]가 있으면(간선이 존재하면) dfs진행
  for j in range(N):
    if not visited[j] and arr[idx][j]:
      visited[j] = 1
      dfs(j)

for i in range(N):
  # 매 행마다 visited 초기화 해주고 dfs로 방문 가능 여부 탐색
  visited = [0] * N
  dfs(i)
  for k in range(N):
    # visited[k]가 True라는 것은 i에서k로 가는 경로가 있다는 뜻이니까 1 출력
    if visited[k]:
      print(1, end=' ')
    else: print(0, end=' ')
  print()
