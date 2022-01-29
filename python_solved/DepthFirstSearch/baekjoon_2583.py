##### 영역 구하기 #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10000)

M, N, K = map(int,input().split())
pos = [list(map(int,input().split())) for _ in range(K)]

def dfs(x, y):
  global cnt
  # 배열에 빈칸(1)이 있으면 0으로 만들어 주고 빈칸의 개수를 더해줌
  if arr[x][y]:
    arr[x][y] = 0
    cnt += 1
    # 4 가지 방향 탐색
    if x - 1 >= 0 and arr[x - 1][y]:
      dfs(x - 1, y)
    if x + 1 < M and arr[x + 1][y]:
      dfs(x + 1, y)
    if y - 1 >= 0 and arr[x][y - 1]:
      dfs(x, y - 1)
    if y + 1 < N and arr[x][y + 1]:
      dfs(x, y + 1)
# 빈 곳을 셀 것이기 때문에 모두 1인 배열 생성
arr = [[1] * N for _ in range(M)]
# 각 직사각형(k)를 돌며 표시
for k in pos:
  # 직 사각형 꼭짓점 좌표 지정해주고
  leftDown_x = k[0]
  leftDown_y = k[1]
  rightUp_x = k[2]
  rightUp_y = k[3]
  # 좌측 상단에서 우측 하단까지 돌며 직사각형을 0으로 표시
  for i in range(M - rightUp_y, M - leftDown_y):
    for j in range(leftDown_x, rightUp_x):
      arr[i][j] = 0

cnt = 0
answers = []
# 배열 돌면서 빈칸이면(1이면)
for i in range(M):
  for j in range(N):
    if arr[i][j]:
      # 빈칸의 개수(크기)는 dfs로 0만들면서 세주고 answers에 추가 후 cnt 초기화
      dfs(i, j)
      answers.append(str(cnt))
      cnt = 0
# 출력 양식대로 출력
answers.sort(key=lambda x: int(x))
print(len(answers))
print(' '.join(answers))