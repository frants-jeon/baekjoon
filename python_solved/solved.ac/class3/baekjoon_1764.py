##### 듣보잡 #####
from sys import stdin
input = stdin.readline
N, M = map(int,input().split())
never_heard = set([input().strip() for _ in range(N)])
never_seen = set([input().strip() for _ in range(M)])
answer = sorted(list(never_seen & never_heard))
print(len(answer))
for name in answer:
  print(name)
