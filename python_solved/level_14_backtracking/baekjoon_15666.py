##### N과 M(12) #####
# https://www.acmicpc.net/problem/15666
N,M = map(int,input().split())
arr = sorted(set(map(int,input().split())))
def dfs(n, ans):
  if n == M:
    print(*ans)
    return
  
  for i in range(len(arr)):
    if n == 0 or ans[-1] <= arr[i]:
      ans.append(arr[i])
      dfs(n + 1, ans)
      ans.pop()

dfs(0, [])