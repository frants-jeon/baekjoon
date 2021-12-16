##### 킹 #####
from sys import stdin
input = stdin.readline
king_pos, stone_pos, N = map(str,input().split())
N = int(N)
move = [input().strip() for _ in range(N)]
alphabet = 'ABCDEFGH'
board = [[f'{alphabet[y]}{x}' for y in range(8)] for x in range(1, 9)]
direction = ['R', 'L', 'T', 'B', 'RT', 'RB', 'LT', 'LB']
dx, dy = [0, 0, 1, -1, 1, -1, 1, -1],[1, -1, 0, 0, 1, 1, -1, -1]

def chess_move(k_pos, s_pos, M):
  k_row, k_column = int(k_pos[1]) - 1, int(alphabet.index(k_pos[0]))
  s_row, s_column = int(s_pos[1]) - 1, int(alphabet.index(s_pos[0]))
  for i in range(N):
    m_idx = direction.index(move[i])
    tmp = [0, 0]
    if ((dx[m_idx] < 0 and k_row > 0) or (dx[m_idx] > 0 and k_row < 7) or dx[m_idx] == 0) and \
      ((dy[m_idx] < 0 and k_column > 0) or (dy[m_idx] > 0 and k_column < 7) or dy[m_idx] == 0):
      k_row += dx[m_idx]
      k_column += dy[m_idx]
    else: continue
    if s_row == k_row + tmp[0] and s_column == k_column + tmp[1]:
      if (s_row == 0 and dx[m_idx] == -1 ) or (s_row == 7 and dx[m_idx] == 1) \
        or (s_column == 0 and dy[m_idx] == -1) or (s_column == 7 and dy[m_idx] == 1):
        k_row -= dx[m_idx]
        k_column -= dy[m_idx]
      else:
        s_row += dx[m_idx]
        s_column += dy[m_idx]

  return [board[k_row][k_column], board[s_row][s_column]]

answer = chess_move(king_pos, stone_pos, move)
print(answer[0])
print(answer[1])
