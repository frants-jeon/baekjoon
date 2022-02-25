##### 암호 만들기 #####
L, C = map(int,input().split())
posibility = sorted(list(input().split()))

def backtracking(idx, ls, vowel, consonant, visited):
  # 조건 맞으면 출력
  if len(ls) == L:
    if consonant >= 2 and vowel >= 1:
      print(''.join(ls))
      return

  for i in range(idx, C):
    # 방문한 적이 없으면 list에 추가 후 모음or자음 갯수 카운팅
    if not visited[i]:
      visited[i] = 1
      ls.append(posibility[i])
      if posibility[i] in {'a','e','i','o','u'}:
        vowel += 1
      else: consonant += 1
      # 백트래킹으로 나머지 자리 탐색
      backtracking(i + 1, ls, vowel, consonant, visited)
      # 나중에 다시 방문 가능하므로 방문 기록 초기화.
      visited[i] = 0
      lp = ls.pop()
      if lp in {'a','e','i','o','u'}:
        vowel -= 1
      else: consonant -= 1

backtracking(0, [], 0, 0, [0] * C)
