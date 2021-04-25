new_list = []
for i in range(0,100):
    elem = int(input())
    new_list.append(elem)

print(max(new_list))
print(new_list.index(max(new_list))+1)