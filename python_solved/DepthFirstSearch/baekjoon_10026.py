##### 적록색약 #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

def dfs(x, y, color, changeTo):
  # 배열에 빈칸(1)이 있으면 0으로 만들어 주고 빈칸의 개수를 더해줌
  if arr[x][y] == color:
    # 색약과 아닌 사람의 답을 따로 구해야 하기 때문에 before, after를 변수로 지정하여 확인
    arr[x][y] = changeTo
    # 4 가지 방향 탐색
    if x - 1 >= 0 and arr[x - 1][y] == color:
      dfs(x - 1, y, color, changeTo)
    if x + 1 < N and arr[x + 1][y] == color:
      dfs(x + 1, y, color, changeTo)
    if y - 1 >= 0 and arr[x][y - 1] == color:
      dfs(x, y - 1, color, changeTo)
    if y + 1 < N and arr[x][y + 1] == color:
      dfs(x, y + 1, color, changeTo)

'''
answer[1]이 적녹색약인 사람의 답, answer[0]이 아닌 사람의 답.
먼저 녹색과 적색의 구역 수를 각각 구해서 [0]에 더해주고 모두 0으로 만듬
그리고 0인 구역의 수를 구해서 [1]에 더해주면 파랑색 구역만 남음.
나머지 파란색 구역을 세어 주고 각각 더해주면 끝.
'''
answer = [0, 0]
cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'G':
      dfs(i, j, 'G', 0)
      cnt += 1
answer[0] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'R':
      dfs(i, j, 'R', 0)
      cnt += 1
answer[0] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 0:
      dfs(i, j, 0, 1)
      cnt += 1
answer[1] += cnt

cnt = 0
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'B':
      dfs(i, j, 'B', 1)
      cnt += 1
answer[1] += cnt
answer[0] += cnt

# 출력 양식대로 출력
for a in answer:
  print(a, end=' ')