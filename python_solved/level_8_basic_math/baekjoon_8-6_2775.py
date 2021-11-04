# #시간초과
# def live_many(k, n):
#     if n == 1:
#         return 1
#     elif k == 0:
#         return n
#     return live_many(k - 1, n) + live_many(k, n - 1)
# T = int(input())
# for i in range(T):
#     k = int(input())
#     n = int(input())
#     print(live_many(k, n))


#답안 서치
t = int(input())
for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력