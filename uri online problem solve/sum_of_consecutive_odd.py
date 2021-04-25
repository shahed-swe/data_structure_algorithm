n = int(input())
m = int(input())
new_list = []



if n < m:
    for i in range(n+1,m):
        if i % 2 != 0:
            new_list.append(i)
else:
    for i in range(m+1,n):
        if i % 2 != 0:
            new_list.append(i)
print(sum(new_list))
