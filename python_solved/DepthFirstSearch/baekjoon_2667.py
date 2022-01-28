##### 단지번호붙이기 #####
from sys import stdin
input = stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

def dfs(x, y):
  global cnt
  # 배열에 집이 있으면 0으로 만들어 주고 집의 개수를 더해줌
  if arr[x][y]:
    arr[x][y] = 0
    cnt += 1
    # 4 가지 방향 탐색
    if y - 1 >= 0 and arr[x][y - 1] == '1':
      dfs(x, y - 1)
    if y + 1 < N and arr[x][y + 1] == '1':
      dfs(x, y + 1)
    if x - 1 >= 0 and arr[x - 1][y] == '1':
      dfs(x - 1, y)
    if x + 1 < N and arr[x + 1][y] == '1':
      dfs(x + 1, y)

answers = []
cnt = 0
# 배열 돌면서 집이 있으면('1'이면)
for i in range(N):
  for j in range(N):
    if arr[i][j] == '1':
      # 이어진 집은 dfs로 0만들면서 개수 세주고 answers에 추가 후 cnt 초기화
      dfs(i, j)
      answers.append(cnt)
      cnt = 0
# 출력 양식대로 출력
answers.sort()
print(len(answers))
for answer in answers:
  print(answer)