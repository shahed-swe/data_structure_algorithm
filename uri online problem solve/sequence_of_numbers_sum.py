sum = 0
while True:
    n,m = map(int, input().split())
    if n <= 0 or m <= 0:
        break
    else:
        if n < m:
            for i in range(n,m+1):
                sum += i
                print("{}".format(i), end=" ")
            print("Sum={}".format(sum))
        else:
            for i in range(m,n+1):
                sum += i
                print("{}".format(i), end=" ")
            print("Sum={}".format(sum))
    sum = 0