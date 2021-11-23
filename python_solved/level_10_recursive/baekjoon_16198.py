N = int(input())
W = list(map(int,input().split()))

total_energy = 0
def save_energy(w):
    global total_energy
    w_lan = len(w)
    if w_lan == 2:
        return
    energy_list = []
    for i in range(1, w_lan - 1):
        energy_list.append(w[i - 1] * w[i + 1])
    small_index = w.index(min(w[1:-1]))
    small = w[small_index - 1] * w[small_index + 1]

    if small >= max(energy_list):
        total_energy += small
        w.remove(w[small_index])
    else:
        total_energy += max(energy_list)
        w.remove(w[energy_list.index(max(energy_list)) + 1])

    save_energy(w)

save_energy(W)
print(total_energy)