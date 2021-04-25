for i in range(int(input())):
    elem = int(input())
    if elem > 0:
        if elem % 2 != 0:
            print("ODD POSITIVE")
        else:
            print("EVEN POSITIVE")
    elif elem < 0:
        if elem % 2 != 0:
            print("ODD NEGATIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        print("NULL")