from itertools import combinations

N, S = map(int,input().split())
li = list(map(int,input().split()))

# cnt, num_pick = 0, 1
# while num_pick <= N:
#     for com in combinations(li, num_pick):
#         if sum(com) == S:
#             cnt += 1
#     num_pick += 1

# print(cnt)
cnt = 0
def backtracking(current, suum):
    global cnt
    if current == N:
        return
    if suum + li[current] == S:
        cnt += 1
    backtracking(current + 1, suum)
    backtracking(current + 1, suum + li[current])

backtracking(0, 0)
print(cnt)