##### RGB거리 #####
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(2000)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def bottom_up():
  dp = [[0,0,0] for _ in range(N)]
  dp[0] = arr[0]
  for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]
  print(min(dp[-1]))

def top_down():
  dp = [[0,0,0] for _ in range(N)]
  def cache(n, color): # n번째 집, color는 RGB순으로 0,1,2
    if dp[n][color] != 0:
      return dp[n][color]
    if n == 0:
      return arr[0][color]
    
    dp[n][color] = min(cache(n - 1, (color + 1) % 3),\
      cache(n - 1, (color + 2) % 3)) + arr[n][color]
    return dp[n][color]
  
  print(min(cache(N - 1, 0), cache(N - 1, 1), cache(N - 1, 2)))

top_down()