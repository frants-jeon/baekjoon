while 1:
    l = list(map(int,input().split()))
    m = max(l)
    if m == 0:
        break
    l.remove(m)
    if l[0] ** 2 + l[1] ** 2 == m ** 2:
        print('right')
    else:
        print('wrong')