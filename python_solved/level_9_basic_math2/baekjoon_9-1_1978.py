N = int(input())
cnt = 0 # 소수 개수 카운팅
num_list = list(map(int,input().split()))
for num in num_list:
    remainder = 0
    if num > 1:    
        for i in range(2,num):
            if num % i == 0:
                remainder += 1
        if remainder == 0:
            cnt += 1
        remainder = 0
print(cnt)