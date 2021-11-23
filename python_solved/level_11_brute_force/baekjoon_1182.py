N, S = map(int,input().split())
l = list(map(int,input().split()))
pick = [False] * N

total = 0
def partial_sequence(sequence, true_cnt, n, boolean):
    sum_sequence = 0
    if true_cnt == n:
        return
    for i in range(n):
        if not boolean[i]:
            boolean[i] = True
        sum_sequence += sequence[i]