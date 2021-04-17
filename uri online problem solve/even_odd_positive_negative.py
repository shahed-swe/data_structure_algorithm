def checker(num):
    even = []
    odd = []
    positive = []
    negative = []

    for i in num:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            pass
    
    return len(even),len(odd), len(positive), len(negative)

if __name__ == '__main__':
    new_list = []
    for i in range(0,5):
        num = int(input())
        new_list.append(num)
    e,d,p,n = checker(new_list)
    print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(e,d,p,n))
"""
-5
0
-3
-4
12
"""
