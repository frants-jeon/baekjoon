##### 교환 #####
from collections import deque

N, K = map(int,input().split())
num_list = list(str(N))
num_len = len(num_list)


def bfs(start):
  que = deque([start])
  # visited[i][j] = i번 교환했을 때 숫자j를 만들 수 있는지 여부 저장
  visited = [[0] * 1000000 for _ in range(K + 1)] 
  is_in_que = [0] * 1000000 # 숫자i가 큐에 들어가 있는지의 여부 저장
  for k in range(K + 1):
    for _ in range(len(que)):
      cur_num = que.popleft() # current_num
      is_in_que[cur_num] = 0
      cur_str_list = list(str(cur_num))
      # k번째 교환으로 만든 적이 없는 숫자면 방문처리 하고 이어서 탐색
      if not visited[k][cur_num]:
        visited[k][cur_num] = 1
        # 각 자릿수를 교환하면서 큐에 없는 숫자면 큐에 추가
        for i in range(num_len):
          for j in range(i + 1, num_len):
            if i == 0 and cur_str_list[j] == '0': continue
            next_num = exchange(cur_num, i, j)
            if not is_in_que[next_num]:
              que.append(next_num)
              is_in_que[next_num] = 1
  # K번 교환했을 때 가장 큰 숫자(1이 포함된 마지막 인덱스) 반환
  answer = ''.join(map(str,visited[K])).rfind('1')
  return answer


def exchange(n, a_idx, b_idx):
  l = list(str(n))
  l[a_idx], l[b_idx] = l[b_idx], l[a_idx]
  return int(''.join(l))


try:
  if N < 100: # 1~2 자리일 때 교환 가능하면 bfs 진행 후 출력
    exchange(N, 0, 1)
  print(bfs(N)) # N == 1,000,000이면 에러 발생
except:
  if N == 1000000:
    print(1000000)
  else: # 교환 불가능한 경우
    print(-1)