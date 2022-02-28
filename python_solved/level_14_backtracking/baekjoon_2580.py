##### 스도쿠 #####
##### https://www.acmicpc.net/problem/2580

board = []
r_check = [[0] * 10 for _ in range(9)] # r_check[i][n] = i번째 행에 n이라는 숫자가 들어있는지 체크
c_check = [[0] * 10 for _ in range(9)] # c_check[i][n] = i번째 열에 n이라는 숫자가 들어있는지 체크
box_check = [[0] * 10 for _ in range(9)] # (3 * 3)의 박스 안에 n이라는 숫자가 들어있는지 체크
zero_list = []
for i in range(9):
  tmp = list(map(int,input().split()))
  board.append(tmp)
  for j in range(9):
    if tmp[j] == 0:
      # 빈칸이 있는 경우 빈칸 좌표 저장
      zero_list.append([i,j])
    else:
      # 빈칸이 아닌경우 행,열,박스에 해당 숫자가 있다고 체크
      r_check[i][tmp[j]] = 1
      c_check[j][tmp[j]] = 1
      box_check[i // 3 * 3 + j // 3][tmp[j]] = 1


def dfs(zero_pos_idx, board, r_check, c_check, box_check):
  # 빈칸을 다 채웠으면 출력 후 프로그램 종료
  if zero_pos_idx == len(zero_list):
    print('-----------')
    for l in range(9):
      print(' '.join(map(str, board[l])))
    exit(0)

  i, j = zero_list[zero_pos_idx] # 빈칸의 좌표 분해 할당
  # 1부터 9까지 숫자 하나씩 넣어봄
  for num in range(1, 10):
    # num과 같은 행,열,박스에 같은 숫자가 없으면 백트래킹 진행
    if not(r_check[i][num] or c_check[j][num] or box_check[i // 3 * 3 + j // 3][num]):
      # 보드에 해당 숫자 넣어주고 행,열,박스에 num이 있다고 체크
      board[i][j] = num
      r_check[i][num] = c_check[j][num] = box_check[i // 3 * 3 + j // 3][num] = 1

      dfs(zero_pos_idx + 1, board, r_check, c_check, box_check) # 다음 빈칸 탐색
      # 탐색 후 돌아왔으면 다른 숫자도 넣어볼 수 있게 원복
      r_check[i][num] = c_check[j][num] = box_check[i // 3 * 3 + j // 3][num] = 0
      board[i][j] = 0

  return

dfs(0, board, r_check, c_check, box_check)

