##### N-Queen #####
n = int(input())
c = [0] * n # 같은 열에 퀸이 있는지 체크
d1 = [0] * (2 * n - 1) # 우상향 대각선에 퀸이 있는지 체크
d2 = [0] * (2 * n - 1) # 우하향 대각선에 퀸이 있는지 체크
answer = 0

def dfs(i): # i는 행 idx
  global answer
  # 모든 행을 다 돌았으면 갯수 세어주고 리턴
  if i == n:
    answer += 1
    return
  # 이번 행의 열을 하나씩 돌면서
  for j in range(n):
    # 같은 열, 대각선에 퀸이 없으면 놓아주고(방문 체크) 탐색하고 다시 방문 초기화(백트래킹)
    if not (c[j] or d1[i+j] or d2[i-j+n-1]):
        c[j] = d1[i+j] = d2[i-j+n-1] = 1
        dfs(i+1)
        c[j] = d1[i+j] = d2[i-j+n-1] = 0

dfs(0) 
print(answer)