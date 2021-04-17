new_list = []
for i in range(0,6):
    n = input()
    if float(n) >= 0:
        new_list.append(n)
    else:
        pass
print("{} valores positivos".format(len(new_list)))