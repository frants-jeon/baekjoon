def warp(n):
    halp = n // 2 # 거리의 반
    distance = 0 # 총 이동 거리
    move = 0 # 한 번에 움직이는 거리
    while distance + move < halp: # 
        move += 1
        distance += move
    if n - distance >= distance + move + 1: # 남은 거리가 move + 1보다 길면 
        distance = distance * 2 + move + 1
        move = move * 2 + 1
    else: 
        distance *= 2
        move *= 2
    if n - distance != 0:
        return move + 1
    else: return move
    

T = int(input())
for _ in range(T):
    x, y = map(int,input().split())
    length = y - x
    print(warp(length))
