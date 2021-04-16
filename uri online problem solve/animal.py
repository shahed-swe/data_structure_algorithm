new_dict = {
    "vertebrado": {
        "ave":{
            "carnivoro": "aguia",
            "onivoro": "pomba",
        },
        "mamifero":{
            "onivoro":"homem",
            "herbivoro":"vaca",
        }
    },
    "invertebrado":{
        "inseto":{
            "hematofago":"pulga",
            "herbivoro":"lagarta",
        },
        "anelideo":{
            "hematofago":"sanguessuga",
            "onivoro":"minhoca",
        }
    }
}
first_name = input()
second_name = input()
third_name = input()

print(new_dict[first_name][second_name][third_name])