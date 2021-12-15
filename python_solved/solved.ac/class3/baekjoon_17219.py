##### 비밀번호 찾기 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
arr = {}
for i in range(N):
  site, password = map(str,input().split())
  arr[site] = password
answers = [input().strip() for _ in range(M)]
for answer in answers:
  print(arr[answer])
