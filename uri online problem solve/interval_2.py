n = int(input())
inside = 0
outside = 0
for i in range(0,n):
    x = int(input())
    if x >= 10 and x <=20:
        inside += 1
    else:
        outside += 1
print(f"{inside} in\n{outside} out")