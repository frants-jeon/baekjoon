N, M = map(int,input().split())
l = sorted(list(map(int,input().split())))
sum_list = [0]

for i in range(N):
    if i < N - 2:
        s = l[i] + l[i + 1] + l[i + 2]
        if s > M:
            break
    for j in range(i + 1, N):
        if j < N - 1:
            s = l[i] + l[j] + l[j + 1]
            if s > M:
                break
        for k in range(j + 1, N):
            s = l[i] + l[j] + l[k]
            if s <= M and s > max(sum_list):
                sum_list.append(s)

print(max(sum_list))