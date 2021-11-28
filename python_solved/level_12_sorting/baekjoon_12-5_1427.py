##### 소트인사이드 #####
N = input()
n_list = []
for i in range(len(N)):
    n_list.append(N[i])
n_list.sort(reverse=True)
re_sort_n = ''.join(n_list)
print(int(re_sort_n))