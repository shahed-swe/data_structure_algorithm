connect = True
while connect == True:
    cont, media, new_cal = 0,0,3
    while cont < 2:
        value = float(input())
        if 0 <= value <= 10:
            cont += 1
            media += value
        else:
            print("nota invalida")       
    print("media = {:.2f}".format(media/2))
    while (new_cal != 1 and new_cal != 2):
        new_cal = int(input("novo calculo (1-sim 2-nao)\n"))
        if new_cal == 1:
            connect = True
        elif new_cal == 2:
            connect = False
        else:
            new_cal = int(input("novo calculo (1-sim 2-nao)\n"))
