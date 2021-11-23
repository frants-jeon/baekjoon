N = int(input())
candy_list = []
case = []
for _ in range(N):
    candy_list.append(list(input()))

def eat_candy(n, candy_list):
    for candy_line in candy_list:
        same_candy = 1
        same_candy_max = 1
        for r in range(len(candy_line) - 1):
            if candy_line[r] == candy_line[r + 1]:
                same_candy += 1
            elif same_candy >= same_candy_max:
                same_candy_max = same_candy
                same_candy = 1
            if same_candy >= same_candy_max:
                same_candy_max = same_candy
                
        check_case.append(same_candy_max)
    # zip 사용해서 세로 행 찾기

    column_list = list(zip(*candy_list))
    for column in column_list:
        same_candy = 1
        same_candy_max = 1
        for c in range(len(column) - 1):
            if column[c] == column[c + 1]:
                same_candy += 1
            elif same_candy >= same_candy_max:
                same_candy_max = same_candy
                same_candy = 1
            if same_candy >= same_candy_max:
                same_candy_max = same_candy
        check_case.append(same_candy_max)
            
    # for r in range(len(column_list)):
    case.append(max(check_case))
    


for i in range(N):
    for j in range(N):
        if j <= N - 2:
            if candy_list[i][j] != candy_list[i][j + 1]:
                candy_list[i][j], candy_list[i][j + 1] = candy_list[i][j + 1], candy_list[i][j]
                check_case = []
                eat_candy(N, candy_list)
                candy_list[i][j], candy_list[i][j + 1] = candy_list[i][j + 1], candy_list[i][j]
        
            if candy_list[j][i] != candy_list[j + 1][i]:
                candy_list[j][i], candy_list[j + 1][i] = candy_list[j + 1][i], candy_list[j][i]
                check_case = []
                eat_candy(N, candy_list)
                candy_list[j][i], candy_list[j + 1][i] = candy_list[j + 1][i], candy_list[j][i]


print(max(case))

