##### 좋은순열 #####

def check_good(s): # 좋은순열인지 체크
  # 뒤에서부터 한 글자씩 늘려가며 인접한 부분수열이 동일한지 체크
  s_len = len(s)
  s1 = s_len - 1
  s2 = s_len - 2
  while s2 >= 0:
    if s[s1:] == s[s2:s1]:
      return False
    s1 -= 1
    s2 -= 2
  return True

def dfs(s):
  global N
  # s는 이미 좋은순열인지 확인했으므로 N 자릿수가 됐다면 출력
  if len(s) == N:
    print(s)
    exit(0)
  # 숫자가 낮은 것부터 출력해야 하니 1,2,3 순서대로 넣어봄
  for new in ['1','2','3']:
    # 마지막 숫자와 넣으려는 숫자가 동일하면 패스
    if s[-1] == new: continue
    # 숫자를 넣었을 때도 좋은순열이라면 이어서 탐색
    if check_good(s + new):
      dfs(s + new)

N = int(input())
dfs('1')


