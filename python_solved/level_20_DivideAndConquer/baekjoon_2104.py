##### 부분배열 고르기 #####
from sys import stdin

input = stdin.readline
N = int(input())
arr = list(map(int,input().split()))

def array_choice(arr: list):
    size = len(arr)
    if size == 1:
        return pow(arr[0], 2)
    center_idx = size // 2
    pointer = [center_idx, center_idx]
    choice_cnt = 1
    choice_min = arr[center_idx]
    current_sum = arr[center_idx]
    max_score = pow(arr[center_idx], 2)
    while choice_cnt < size:
        choice_cnt += 1
        if pointer[0] == 0:
            pointer[1] += 1
            choice_min = min(choice_min, arr[pointer[1]])
            current_sum += arr[pointer[1]]
        elif pointer[1] == size - 1:
            pointer[0] -= 1
            choice_min = min(choice_min, arr[pointer[0]])
            current_sum += arr[pointer[0]]
        elif arr[pointer[0] - 1] >= arr[pointer[1] + 1]:
            pointer[0] -= 1
            choice_min = min(choice_min, arr[pointer[0]])
            current_sum += arr[pointer[0]]
        else:
            pointer[1] += 1
            choice_min = min(choice_min, arr[pointer[1]])
            current_sum += arr[pointer[1]]
        max_score = max(max_score, current_sum * choice_min)

    left_max = array_choice(arr[:center_idx])
    right_max = array_choice(arr[center_idx:])
    answer = max(max_score, left_max, right_max)
    return answer

print(array_choice(arr))