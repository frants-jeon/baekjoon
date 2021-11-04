

###########################################################
# 시간초과
import copy

N = int(input())
disk = {}
move = []
stick = {1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
for i in range(1, N + 1):
    disk[i] = 1


def check_value(comparator): # disk에서 원하는 value 값에 해당하는 키값들 반환
    fake_disk = copy.deepcopy(disk)
    for i in list(fake_disk.keys()):
        if fake_disk[i] != comparator:
            del fake_disk[i]
    if len(fake_disk.keys()) == 0:
        return [100]
    else:
        return fake_disk.keys()



def hanoi(n, destination):
# 이동 불가 :n의 현재 위치(value)에서 n이 최솟값이 아니거나 destination에서 제일 작은 값이 n 보다 작을 때
    if min(check_value(disk[n])) != n or min(check_value(destination)) < n :
        hanoi(n - 1, stick[destination + disk[n - 1]])
    # 이동 가능 :n의 현재 위치(value)에서 n이 최솟값이고 destination에서 제일 작은 값이 n 보다 클 때
    if min(check_value(disk[n])) == n and min(check_value(destination)) > n :
        old = disk[n]
        disk[n] = destination
        move.append(f'{old} {disk[n]}')
        if n != 1:
            hanoi(n - 1, disk[n])
        elif n == 1:
            return

hanoi(N, 3)
print(len(move))
for i in move:
    print(i)
N = int(input())

# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#         pass
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, c)
#         hanoi(n - 1, b, a, c)

# hanoi(N, 1, 2, 3)
# print(2 ** N - 1)
