##### 히스토그램 #####
from sys import stdin
input = stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
left = 0
right = 1
def histogram(arr):
    global left, right
    size = len(arr)
    if size == 1:
        return arr[0]
    divider_idx = size // 2
    pointer = [divider_idx, divider_idx]
    width = 1
    height = arr[divider_idx]
    max_area = width * height
    while width < size:
        # 제일 왼쪽까지 갔을 때
        if pointer[left] == 0:
            width += 1
            # 오른쪽 높이가 더 낮을 때
            if arr[pointer[right] + 1] < height:
                height = arr[pointer[right] + 1]
                pointer[right] += 1
            else:
                pointer[right] += 1
            if height * width > max_area and height * width <= 2000000000:
                max_area = height * width
        # 제일 오른쪽까지 갔을 때
        elif pointer[right] == size - 1:
            width += 1
            # 왼쪽 높이가 더 낮을 때
            if arr[pointer[left] - 1] < height:
                height = arr[pointer[left] - 1]
                pointer[left] -= 1
            else:
                pointer[left] -= 1
            if height * width > max_area and height * width <= 2000000000:
                max_area = height * width
        # 왼쪽이 더 크거나 같을 때
        elif arr[pointer[left] - 1] >= arr[pointer[right] + 1]:
            width += 1
            # 왼쪽 높이가 더 낮을 때
            if arr[pointer[left] - 1] < height:
                height = arr[pointer[left] - 1]
                pointer[left] -= 1
            else:
                pointer[left] -= 1
            if height * width > max_area and height * width <= 2000000000:
                max_area = height * width
        # 오른쪽이 더 클 때
        else:
            width += 1
            # 오른쪽 높이가 더 낮을 때
            if arr[pointer[right] + 1] < height:
                height = arr[pointer[right] + 1]
                pointer[right] += 1
            else:
                pointer[right] += 1
            if height * width > max_area and height * width <= 2000000000:
                max_area = height * width
    left_max = histogram(arr[:divider_idx])
    right_max = histogram(arr[divider_idx:])
    answer = max(max_area, left_max, right_max)
    return answer

print(histogram(arr))