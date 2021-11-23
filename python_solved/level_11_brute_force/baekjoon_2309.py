nanjang = []
for _ in range(9):
    nanjang.append(int(input()))
nanjang.sort()
delete_index = []
for i in range(len(nanjang) - 1):
    for j in range(i + 1, len(nanjang)):
        height_check = 0
        height_list = []
        for k in range(9):
            if k in [i, j]:
                continue
            if height_check <= 100:
                height_check += nanjang[k]
                height_list.append(nanjang[k])
            else: break
        if height_check == 100:
            break
    if height_check == 100:
        break


for height in height_list:
    print(height)