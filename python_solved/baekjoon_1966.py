##### 프린터 큐 #####
from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):
  N, M = map(int,input().split())
  arr = list(enumerate(list(map(int,input().split()))))
  answer = 0
  while len(arr) > 0:
    arr_max = max(arr, key= lambda x: x[1])
    if arr[0] == arr_max:
      arr.remove(arr_max)
      answer += 1
      if arr_max[0] == M:
        break
    else: arr.append(arr.pop(0))
    
  print(answer)