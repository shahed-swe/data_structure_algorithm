import random
new_list = []
while True:
    num = random.randint(0,4000)
    if num not in new_list:
        new_list.append(num)
        if len(new_list) == 3999:
            break
        else:
            pass
print(len(new_list))
print(new_list)