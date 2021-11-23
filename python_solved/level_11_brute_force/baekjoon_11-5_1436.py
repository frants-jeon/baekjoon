##### 영화감독 숌 #####
N = int(input())
devil_num = 666
movie_title = 0
while movie_title < N:
    find666 = str(devil_num).find('666')
    if find666 != -1:
        movie_title += 1
        devil_num += 1
    else:
        devil_num += 1
print(devil_num - 1)