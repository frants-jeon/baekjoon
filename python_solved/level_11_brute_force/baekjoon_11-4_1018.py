##### 체스판 다시 칠하기 #####
# 8 * 8 체스판이 몇 개인지 구해서 두 종류의 체스판과 비교하여 다른 칸의 개수를 세서 저장. min값 추출

row, column = map(int,input().split())
chess = []
for _ in range(row):
    chess.append(input())

correct_chess1 = []
for _ in range(4):
    correct_chess1.append('WBWBWBWB')
    correct_chess1.append('BWBWBWBW')

correct_chess2 = []
for _ in range(4):
    correct_chess2.append('BWBWBWBW')
    correct_chess2.append('WBWBWBWB')

def get_chess(whole_chess, start_row, start_column):
    check_chess = []
    for i in range(start_row, start_row + 8):
        check_chess.append(whole_chess[i][start_column: start_column + 8])
    return check_chess

def check_diff(check_chess, compare_chess1, compare_chess2):
    if len(check_chess) != 8:
        return False
    compare_chess1_diff = 0
    compare_chess2_diff = 0
    for i in range(len(check_chess)):
        for j in range(len(check_chess)):
            if check_chess[i][j] != compare_chess1[i][j]:
                compare_chess1_diff += 1
            if check_chess[i][j] != compare_chess2[i][j]:
                compare_chess2_diff += 1
    return (compare_chess1_diff, compare_chess2_diff)

diff_list = []
for r_start in range(row - 7):
    for c_start in range(column - 7):
        cnt1, cnt2 = check_diff(get_chess(chess, r_start, c_start), correct_chess1, correct_chess2)
        if cnt1 > cnt2:
            diff_list.append(cnt2)
        else:
            diff_list.append(cnt1)



print(min(diff_list))