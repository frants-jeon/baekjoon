h, m = map(int,input().split())
if m - 45 >= 0 :
    print(h,m-45)
elif h == 0 :
    h = 23
    m = m + 60 - 45
    print(h,m)
else:
    h -= 1
    m = m + 60 - 45
    print(h,m)