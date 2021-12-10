##### 수 이어쓰기 #####
import sys
N = sys.stdin.readline().strip('\n')
arr = [int(N[i]) for i in range(len(N) -1, -1, -1)]
arr2 = [9 for _ in range(len(N) + 1)]
arr.insert(0,0)
def write_num(pos, arr):
  if pos == 1:
    return arr[pos]
  tmp = str(arr[pos] - 1)
  for i in range(pos - 1, 0, -1):
    tmp += str(arr[i])
  answer = pos * (int(tmp) + 1) 
  answer += write_num(pos - 1, arr2)
  return answer

print(write_num(len(N), arr))