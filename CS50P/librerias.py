import random

# moneda = random.choice(["cara", "cruz"])
# print(moneda)

# numero = random.randint(1,10)
# print(numero)

cartas = ['jack', 'reina', 'rey']
random.shuffle(cartas)
for carta in cartas:
    print(carta)