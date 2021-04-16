start_hour, start_minute, end_hour, end_minute = map(int, input().split())

difference = ((end_hour * 60 ) + end_minute) - ((start_hour * 60 ) + start_minute)

if difference <= 0:
    difference += 24 * 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(difference // 60, difference % 60))
