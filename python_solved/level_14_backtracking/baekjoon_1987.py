##### 알파벳 #####
from sys import stdin
input = stdin.readline

R, C = map(int,input().split())
# 인풋으로 받은 대문자를 아스키코드로 변경 후 65(A의 ascii코드)를 빼줘서 0 ~ 25로 변환하여 할당
board = [list(map(lambda x: x - 65, map(ord, input().strip()))) for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

def dfs(r, c, visited, cnt):
  global answer
  current = board[r][c]
  # used는 방문한 적 있는 글자인지 확인하는 배열. True면 방문한 적 있다는 뜻
  # 현재 위치를 방문한 적이 있으면 더 갈 수 없으므로 최댓값 갱신 후 리턴
  if visited[current]:
    answer = max(answer, cnt)
    return
  
  # 방문 가능하면 cnt늘려주고 방문처리
  cnt += 1
  visited[current] = True
  # dfs탐색 시작
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < R and 0 <= nc < C:
      dfs(nr, nc, visited, cnt)
  # 백트래킹으로 진행해야 하기 때문에 탐색이 끝난 후 다시 방문할 수 있도록 방문여부와 cnt원복.
  visited[current] = False
  cnt -= 1


dfs(0, 0, [False] * 26, 0)
print(answer)
