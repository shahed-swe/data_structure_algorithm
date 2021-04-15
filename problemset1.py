n = int(input())
new_list = []
for i in range(0,n):
    command = list(map(str, input().split(" ")))
    if command[0] == "insert":
        new_list.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print(new_list)
    elif command[0] == "remove":
        new_list.remove(int(command[1]))
    elif command[0] == "append":
        new_list.append(int(command[1]))
    elif command[0] == "sort":
        new_list.sort()
    elif command[0] == "pop":
        new_list.pop(-1)
    elif command[0] == "reverse":
        new_list.reverse()
    else:
        pass
