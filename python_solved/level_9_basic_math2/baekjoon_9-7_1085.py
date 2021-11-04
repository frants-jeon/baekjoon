x, y, w, h = map(int,input().split())
l = []

x_move = w - x
y_move = h - y
l.append(x_move)
l.append(y_move)
l.append(x)
l.append(y)

print(min(l))