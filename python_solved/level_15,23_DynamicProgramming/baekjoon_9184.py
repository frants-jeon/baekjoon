##### 신나는 함수 실행 #####
from sys import stdin
input = stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 or c > 20:
    dp[20][20][20] = w(20, 20, 20)
    return dp[20][20][20]
  if dp[a][b][c] != 0: return dp[a][b][c]
  if a < b and b < c:
    dp[a][b][c - 1] = w(a, b, c - 1)
    dp[a][b - 1][c - 1] = w(a, b - 1, c - 1)
    dp[a][b - 1][c] = w(a, b - 1, c)
    return dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c]
  else:
    dp[a - 1][b][c] = w(a - 1, b, c)
    dp[a - 1][b - 1][c] = w(a - 1, b - 1, c)
    dp[a - 1][b][c - 1] = w(a - 1, b, c - 1)
    dp[a - 1][b - 1][c - 1] = w(a - 1, b - 1, c - 1)
    return dp[a - 1][b][c] + dp[a - 1][b - 1][c] + dp[a - 1][b][c - 1] - dp[a - 1][b - 1][c - 1]

while 1:
  a, b, c = map(int,input().split())
  if a == -1 and b == -1 and c == -1: break
  print(f'w({a}, {b}, {c}) = {w(a, b, c)}')