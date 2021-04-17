_,start_day = map(str, input().split(" "))
start_time = list(map(int, input().split(":")))
_,end_day = map(str, input().split(" "))
end_time = list(map(int, input().split(":")))

day = int(end_day) - int(start_day)
hour = end_time[0] - start_time[0]
minute = end_time[1] - start_time[1]
seconds = end_time[2] - start_time[2]

if seconds < 0:
    seconds += 60
    minute -= 1

if minute < 0:
    minute += 60
    hour-=1

if hour < 0:
    hour += 24
    day-=1

print("{} dia(s)".format(day))
print("{} hora(s)".format(hour))
print("{} minuto(s)".format(minute))
print("{} segundo(s)".format(seconds))