n = float(input())
tax = 0
if n <= 2000:
    print("Isento")
else:
    if n >= 2000.01 and n <= 3000.00:
        tax = (n - 2000) * 0.08
    elif n >= 3000.01 and n <= 4500.00:
        tax = ((n - 3000) * 0.18) + 80
    else:
        tax = ((n - 4500) * 0.28) + 350
    print("R$ {:.2f}".format(tax))