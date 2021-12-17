##### 오목 #####
from sys import stdin
input = stdin.readline
arr = [list(map(int,input().split())) for _ in range(19)]
arr.insert(0, [0 for _ in range(19)])
for a in range(20):
  arr[a].insert(0,0)

# for ar in arr:
#   print(ar)

def omok(pos, color):
  check = [[],[],[],[]]
  for i in range(6):
    if pos[1] + i < 20:
      check[0].append(arr[pos[0]][pos[1] + i])
    if pos[0] + i < 20:
      check[1].append(arr[pos[0] + i][pos[1]])
    if pos[0] + i < 20 and pos[1] + i < 20:
      check[2].append(arr[pos[0] + i][pos[1] + i])
    if pos[0] - i > 0 and pos[1] + i < 20:
      check[3].append(arr[pos[0] - i][pos[1] + i])
  six_num = []
  back = [[0, -1], [-1, 0], [-1, -1], [1, -1]]
  for j in range(4):
    if len(check[j]) == 6:
      p = check[j].pop()
    else: p = -1
    six_num.append((arr[pos[0] + back[j][0]][pos[1] + back[j][1]], p))
    if six_num[j] == -1:
      if color == 1 and sum(check[j]) == 5 : return 1
      if color == 2 and sum(check[j]) == 10: return 2
    elif color == 1 and sum(check[j]) == 5 and six_num[j][0] != 1 and six_num[j][1] != 1: return 1
    elif color == 2 and sum(check[j]) == 10 and six_num[j][0] != 2 and six_num[j][1] != 2: return 2
  return 0

for i in range(1, 20):
  for j in range(1, 20):
    if arr[i][j] == 0: continue
    answer = omok((i,j), arr[i][j])
    if answer == 1 or answer == 2:
      print(answer)
      print(i, j)
      quit()
print(0)

