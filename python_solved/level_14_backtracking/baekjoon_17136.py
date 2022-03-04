##### 색종이 붙이기 #####

def attach_remove(arr, x, y, size, option):
  # option = 0: 붙이기 / 1:떼기
  for i in range(size):
    for j in range(size):
      arr[x + i][y + j] = option
  return arr


def check_change(arr, x, y, size):
  # 체크할 때 바로 배열을 바꿔가면서 체크하면 전체 배열도 바뀌기 때문에 체크 따로 변경 따로 진행
  cnt = 0
  try:
    for i in range(size):
      for j in range(size):
        # 스티커를 붙여야 하는 자리가 0이면 False
        if arr[x + i][y + j] == 0: return False
        cnt += 1
    # 스티커 크기만큼 붙일 수 있으면 True
    if cnt == pow(size, 2):
      return True
  except: # arr범위 벗어나면 False
    return False 


def dfs(i, j, paper_left, cnt): # 위에서부터 아래로 탐색
  global board, answer
  if j >= 10: # 모든 배열을 다 탐색했으면 최솟값 갱신
    answer = min(answer, cnt)
    return
  if i >= 10: # 이번 열을 다 탐색했으면 다음 열 탐색 시작
    dfs(0, j + 1, paper_left, cnt)
    return

  # 보드가 1이면(스티커를 붙일 수 있으면)
  if board[i][j]:
    # 5부터 1까지 스티커 사이즈를 돌면서
    for size in range(5, 0, -1):
      # 스티커 갯수를 다 사용하지 않았으면
      if paper_left[size] > 0:
        # 이 위치에 해당 스티커를 붙일 수 있는지 체크
        if check_change(board, i, j, size):
          # 가능하면 스티커 붙이고
          paper_left[size] -= 1
          attach_remove(board, i, j, size, 0)
          # 스티커 크기를 지나 다음 줄로 이동하여 탐색
          dfs(i + size, j, paper_left, cnt + 1)
          # 탐색 끝났으면 원복
          paper_left[size] += 1
          attach_remove(board, i, j, size, 1)
  else:
    # 보드가 0이면 다음줄 탐색
    dfs(i + 1, j, paper_left, cnt)


board = [list(map(int,input().split())) for _ in range(10)]
answer = 100
dfs(0, 0, [1,5,5,5,5,5], 0)
print(answer if answer != 100 else -1)