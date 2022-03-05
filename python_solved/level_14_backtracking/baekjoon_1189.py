##### 컴백홈 #####

def dfs(r, c, cnt):
  global answer
  if r == 0 and c == C - 1 and cnt == K:
    answer += 1
    return

  # 방문한 적 없는 좌표면 이동횟수 저장(방문처리)하고 다음 좌표 탐색
  if not board[r][c]:
    board[r][c] = cnt
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
      nr, nc = r + dr, c + dc
      # 이동 가능한 좌표면서 방문한 적 없으면 이어서 탐색
      if 0 <= nr < R and 0 <= nc < C:
        if not board[nr][nc]:
          dfs(nr, nc, cnt + 1)
    # 백트래킹을 위해서 탐색 끝나면 방문 초기화
    board[r][c] = 0
  return

R, C, K = map(int,input().split())
# '.'은 0으로 받고 T는 -1로 받음
board = [[0 if i == '.' else -1 for i in input()] for _ in range(R)]
answer = 0
dfs(R - 1, 0, 1)
print(answer)