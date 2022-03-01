##### 순열장난 #####

def dfs(s, visited):
  global n
  # 문자의 갯수만큼 잘 나눴으면 정답인지 확인
  if len(s) == n:
    # 공백 앞의 문자만 방문처리를 해줬기 때문에 마지막 문자 확인
    # 1부터 n까지 모든 숫자를 방문했고 마지막 숫자가 방문하지 않은 유일한 숫자라면 출력
    last = int(s[-1])
    if sum(visited) + 1 == n and last <= n and not visited[last]:
      print(' '.join(s))
      exit(0)

  # 아직 분리가 안된 문자 꺼내서 백트래킹 시작
  can_div = s.pop()
  # 문자 한 개를 꺼낼 때와 두 개를 꺼낼 때로 나눠서 백트래킹
  for l in range(1, 3):
    cur_num = int(can_div[:l]) # 분리 가능한지 확인할 현재 숫자
    # 현재 숫자가 범위 안에 있고 방문한 적이 없으면 공백 추가하고 방문처리
    if 0 < cur_num <= n:
      if not visited[cur_num]:
        new = can_div.replace(can_div[:l], can_div[:l] + ' ', 1)
        visited[cur_num] = 1
        # 문자를 분리하여 기존 문자열과 합쳐서 탐색
        dfs(s + new.split(), visited)
        # 탐색했으나 정답이 아니면 다시 방문 가능하도록 처리
        visited[cur_num] = 0
  return
  
s = input()
s_len = len(s)
n = s_len if s_len < 10 else (s_len - 9) // 2 + 9 # 문자의 갯수(N) 구하기
dfs([s], [0] * (n + 1))