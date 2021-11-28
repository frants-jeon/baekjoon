from sys import stdin

case_cnt = 1
while 1:
    L, P, V = map(int,stdin.readline().split())
    camping_day = 0
    ban_camping = P - L
    while V > 0:
        if V >= L:
            V -= L
            camping_day += L
        else:
            camping_day += V
            V = 0
        if V >= ban_camping:
            V -= ban_camping
        else:
            V = 0
    if L == 0 and P == 0 and V == 0: break
    print(f'Case {case_cnt}: {camping_day}')
    case_cnt += 1

