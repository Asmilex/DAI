import random

abre = random.randint(1, 5)
cierra = abre
n = abre + cierra

x = ""
balanceado = True

while n > 0:
    if random.random() < 0.5 and abre > 0:
        x = x + "["
        abre = abre - 1
        n = n - 1
    elif cierra > 0:
        x = x + "]"
        cierra = cierra - 1
        n = n - 1

    if cierra < abre:
        balanceado = False

print(x)

if balanceado:
    print("Está correcto")
else:
    print("No está balanceado")
