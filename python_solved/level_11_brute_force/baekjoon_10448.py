N = int(input())
k_list = []
for _ in range(N):
    k_list.append(int(input()))

def ureka(k, t_list):
    for i in t_list:
        for j in t_list:
            for l in t_list:
                triangle = i + j + l
                if triangle == k:
                    return 1
    return 0


for k in k_list:
    t_list = []
    t = 1
    while 1:
        t_sum = 0
        for i in range(1, t + 1):
            t_sum += i
        t_list.append(t_sum)
        t += 1
        if t_sum >= k: break
    print(ureka(k, t_list))

