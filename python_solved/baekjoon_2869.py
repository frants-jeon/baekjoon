##### 달팽이는 올라가고 싶다 #####
A, B, V = map(int,input().split())
oneday = A - B
if (V - A) % oneday == 0:
    date = (V - A) // oneday + 1
else:
    date = (V - A) // oneday + 2
print(date)