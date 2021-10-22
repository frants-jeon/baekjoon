point = int(input('시험 점수를 입력하시오.'))
if point > 0 and point <= 100 :
    if point >= 90 :
        print('A')
    elif point >= 80 :
        print('B')
    elif point >= 70 :
        print('C')
    elif point >= 60 :
        print('D')
    else:
        print('F')
else:
    print('0에서 100 사이의 숫자만 입력하시오.')