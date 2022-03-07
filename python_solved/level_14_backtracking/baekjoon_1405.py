##### 미친 로봇 #####
# https://www.acmicpc.net/problem/1405

def dfs(x, y, left, visited):
  # 이미 방문한 적이 있으면 0 리턴
  if visited[x][y]:
    return 0

  # 이동 횟수를 다 소진했으나 같은 곳을 방문한 적이 없으면 1 리턴
  if left <= 0:
    return 1


  probabiliy = 0 # 확률
  visited[x][y] = 1 # 이번 좌표 방문처리
  for i in range(4): # 4방향 돌면서
    if info[i] > 0: # 이번 방향의 확률이 0보다 크면 다음 좌표 할당
      nx, ny = x + dx[i], y + dy[i]
      if not visited[nx][ny]: # 다음 좌표를 방문한 적이 없으면 계속 탐색
        # 이번 좌표의 확률은 다음 좌표의 확률을 다 더한 것
        probabiliy += dfs(nx, ny, left - 1, visited) * info[i] * 0.01
  visited[x][y] = 0
  return probabiliy 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
info = list(map(int,input().split())) # 4방향 확률
left = info.pop(0) # 남은 이동 횟수
answer = 0
visited = [[0] * 31 for _ in range(31)] # 중앙에서 최대 14번 움직일 수 있도록 배열 생성
for i in range(4):
  answer += dfs(15 + dx[i], 15 + dy[i], left, visited) * info[i] * 0.01

print(answer)