##### 세 수 #####
from sys import stdin
li = list(map(int,stdin.readline().split()))
li.remove(max(li))
print(max(li))