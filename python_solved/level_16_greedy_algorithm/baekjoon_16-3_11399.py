##### ATM #####
from sys import stdin
input = stdin.readline
N = int(input())
P = list(map(int,input().split()))
P.sort()
tmp = 0
answer = []
for i in range(N):
  tmp += P[i]
  answer.append(tmp)
print(sum(answer))