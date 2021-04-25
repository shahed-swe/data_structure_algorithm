n = int(input())
rabbit = 0
rat = 0
frog = 0
total = 0
for i in range(n):
    item, type = map(str, input().split())
    if type == "C":
        rabbit += int(item)
    elif type == "R":
        rat += int(item)
    elif type == "S":
        frog += int(item)
    else:
        pass
    total += int(item)

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(rabbit))
print("Total de ratos: {}".format(rat))
print("Total de sapos: {}".format(frog))
print("Percentual de coelhos: {:.2f} %".format((rabbit / (total * 1.0))*100))
print("Percentual de ratos: {:.2f} %".format((rat / (total * 1.0))*100))
print("Percentual de sapos: {:.2f} %".format((frog / (total * 1.0))*100))
