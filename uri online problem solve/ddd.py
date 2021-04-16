new_dict = {
    61:"Brasilia",
    71:"Salvador",
    11:"Sao Paulo",
    21:"Rio de Janeiro",
    32:"Juiz de Fora",
    19:"Campinas",
    27:"Vitoria",
    31:"Belo Horizonte"
}
number = int(input())
if new_dict.get(number) != None:
    print(new_dict.get(number))
else:
    print("DDD nao cadastrado")
