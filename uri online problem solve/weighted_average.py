n = int(input())
for i in range(n):
    x,y,z = map(float, input().split())
    x = x * 2
    y = y * 3
    z = z * 5
    print("{:.1f}".format((x+y+z)/(10)))
