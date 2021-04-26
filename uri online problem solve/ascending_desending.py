while True:
    n,m = map(int, input().split())
    if n > m:
        print("Decrescente")
    elif m > n:
        print("Crescente")
    else:
        break