##### 석판 자르기 #####
from sys import stdin

input = stdin.readline
N = int(input())
stone_plate = []
for _ in range(N):
    stone_plate.append(list(map(int,input().split())))

def is_answer(arr):
    jewel_cnt = 0
    trash_cnt = 0
    for i in range(len(arr)):
        if arr[i].count(2) > 0:
            jewel_cnt += arr[i].count(2)
            if jewel_cnt > 1:
                break
        if 1 in arr[i]:
            trash_cnt += 1
            break
    if jewel_cnt != 1 or trash_cnt != 0:
        return False
    return True

def divide_plate(arr):
    size = len(arr)
    cut_list = []
    one = 1
    two = 1
    case_cnt = 0
    if size <= 1:
        try:
            size = len(arr[0])
        except:
            size = len(arr)
        for i in range(size):
            line = arr[0][i]
            if line == 1:
                cut_list.append(i)
        if len(cut_list) == 0:
            return is_answer(arr)
        for cut in cut_list:
            if cut != 0:
                one = divide_plate(list([arr[0][:cut]]))
            if cut != size:
                two = divide_plate(list([arr[0][cut + 1:]]))
            case_cnt += one * two
        return case_cnt
        
    else:
        arr = list(zip(*(arr)))
        size = len(arr)
        for i in range(len(arr)):
            line = arr[i]
            if 2 not in line and 1 in line:
                cut_list.append(i)
        if len(cut_list) == 0:
            return is_answer(arr)
        for cut in cut_list:
            if cut != 0:
                one = divide_plate(arr[:cut])
            if cut != size:
                two = divide_plate(arr[cut + 1:])
            case_cnt += one * two
        return case_cnt

if __name__ == "__main__":
    answer_cnt = 0
    answer_cnt += divide_plate(stone_plate)
    stone_plate = list(zip(*stone_plate))
    answer_cnt += divide_plate(stone_plate)
    if answer_cnt == 0:
        print(-1)
    else:
        print(answer_cnt)
