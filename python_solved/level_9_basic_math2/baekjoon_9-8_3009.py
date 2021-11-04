x = []
y = []
for _ in range(3):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)

x_cnt = set(x)
y_cnt = set(y)

for i in x_cnt:
    if x.count(i) == 1:
        print(i, end=' ')
for i in y_cnt:
    if y.count(i) == 1:
        print(i)