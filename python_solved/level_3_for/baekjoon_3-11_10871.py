#3-11문제(서치하여 해결)
n, x = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n): #이까지는 혼자 함.
    if x > a[i] :
        print(a[i],end=' ')