cnt = 0
for i in range(0, 5):
    n = int(input())
    if n < 0:
        n = -1 * n
    if n % 2 == 0:
        cnt+= 1

print("{} valores pares".format(cnt))
