hour, minute, second = map(int,input().split())
D = int(input())

plus_second = D % 60
plus_minute = D // 60 % 60
plus_hour = D // 60 // 60

hour += plus_hour
minute += plus_minute
second += plus_second

if second >= 60:
    second -= 60
    minute += 1
if minute >= 60:
    minute -= 60
    hour += 1
while hour >= 24:
    hour -= 24

print(hour, minute, second)