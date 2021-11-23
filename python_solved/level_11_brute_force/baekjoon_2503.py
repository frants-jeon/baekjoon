arr = [] #현재 가능한 모든 경우의 수
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            arr.append(f'{i}{j}{k}')
# 전체 arr를 돌면서 일치하지 않는 조건은 제외 / 맞는 애들은 arr_temp에 넣고 arr에 덮어쓰기
N = int(input())
questions = []
strike = []
ball = []
arr_temp = []
for i in range(N):
    q, s, b = map(str,input().split())
    questions.append(q)
    strike.append(s)
    ball.append(b)

def is_possibility_num(arr_num, question_num, strike_cnt, ball_cnt):
    answer = True
    strike_position = set()
    for i in range(3):
        if arr_num[i] == question_num[i]:
            strike_position.add(i)
    if len(strike_position) != int(strike_cnt):
        return False

    ball_correct_cnt = 0
    for j in {0,1,2} - strike_position:
        if question_num[j] in arr_num and question_num[j] != arr_num[j]:
            ball_correct_cnt += 1
    if ball_correct_cnt != int(ball_cnt):
        return False
    return answer


for i in range(len(questions)):
    question = questions[i]
    strikei = strike[i]
    balli = ball[i]
    for num in arr:
        if is_possibility_num(num, question, strikei, balli):
            arr_temp.append(num)
    arr = arr_temp
    arr_temp = []

print(len(arr))