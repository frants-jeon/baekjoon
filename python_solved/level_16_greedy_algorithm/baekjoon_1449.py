from sys import stdin

N, L = map(int,stdin.readline().split())
pos = list(map(int,stdin.readline().split()))
pos.sort()

tape = L - 1
cnt = 0
for i in range(len(pos)):
    if i == len(pos) - 1:
        cnt += 1
        break
    step = pos[i + 1] - pos[i]
    if step <= tape:
        tape -= step
        continue
    tape = L - 1
    cnt += 1

print(cnt)