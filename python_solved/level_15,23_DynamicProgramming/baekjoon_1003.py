##### 피보나치 함수 #####
from sys import stdin
input = stdin.readline

def bottom_up():
  T = int(input())
  dp = [[-1, -1] for _ in range(41)]
  dp[0], dp[1] = [1, 0], [0, 1]
  for i in range(2, 41):
    if dp[i - 1] != [-1, -1] and dp[i - 2] != [-1, -1]:
      dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
      dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

  for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])


def top_down():
  dp = [[-1, -1] for _ in range(41)]
  def memoization(n):
    if dp[n] != [-1, -1]: return dp[n]
    if n == 0:
      dp[n] = [1, 0]
      return dp[n]
    if n == 1:
      dp[n] = [0, 1]
      return dp[n]
    
    b1 = memoization(n - 1)
    b2 = memoization(n - 2)
    dp[n][0] = b1[0] + b2[0]
    dp[n][1] = b1[1] + b2[1]
    return dp[n]
  
  for tc in range(int(input())):
    answer = memoization(int(input()))
    print(answer[0], answer[1])
