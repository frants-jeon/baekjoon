##### 나는야 포켓몬 마스터 이다솜 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
arr = [input().strip('\n') for _ in range(N)]
quiz = [input().strip('\n') for _ in range(M)]
num_search = {}
str_search = {}
for i in range(N):
  num_search[i + 1] = arr[i]
  str_search[arr[i]] = i + 1
  
print(quiz)
for j in range(M):
  try:
    print(num_search[int(quiz[j])])
  except:
    print(str_search[quiz[j]])
