n = int(input())
for i in range(n):
    n,m = map(int, input().split())
    try:
        div = n / m
        print("{:.1f}".format(div))
    except:
        print("divisao impossivel")