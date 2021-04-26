sum_make = []
while True:
    value = float(input())
    if value > 0 and value <= 10.0:
        sum_make.append(value)
        if len(sum_make) == 2:
            print("media = {:.2f}".format(sum(sum_make)/2))
            break
    else:
        print("nota invalida")