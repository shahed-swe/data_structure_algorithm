new_list = []
for i in range(0, 6):
    n = input()
    if float(n) >= 0:
        new_list.append(n)
    else:
        pass
print("{} valores positivos".format(len(new_list)))
summation = 0
for i in new_list:
    summation += float(i)
print("{:.1f}".format(summation/len(new_list)))
