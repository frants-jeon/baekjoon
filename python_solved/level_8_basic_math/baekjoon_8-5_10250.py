T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    cnt = 0
    for room in range(1, W + 1):
        for floor in range(1, H + 1):
            cnt += 1
            if cnt == N:
                if room < 10:
                    print(floor,0,room,sep='')
                elif room >= 10:
                    print(floor,room,sep='')
                else:
                    print('오류')