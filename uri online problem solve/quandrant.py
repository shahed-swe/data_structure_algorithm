while True:
    n,m = map(int, input().split())
    if n == 0 or m == 0:
        break
    elif n > 0 and m > 0:
        print("primeiro")
    elif n > 0 and m < 0:
        print("quarto")
    elif n < 0 and m < 0:
        print("terceiro")
    else:
        print("segundo")