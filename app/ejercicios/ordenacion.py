import random
import time

arr = [random.randrange(1, 100, 1) for i in range(random.randint(50, 100))]

def ordenacion_burbuja(lista):
    for i in range (len(lista)):
        for j in range (0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def ordenacion_gnomo(lista):
    if len(lista) > 1:
        index = 0
        while index < len(lista):
            if index == 0:
                index = index + 1
            if lista[index] >= lista[index - 1]:
                index = index + 1
            else:
                lista[index], lista[index - 1] = lista[index - 1], lista[index]
                index = index - 1

# start = time.time()
# ordenacion_burbuja(arr.copy())
# end = time.time()

# print("Burbuja tarda " + str(end - start))

# start = time.time()
# ordenacion_gnomo(arr.copy())
# end = time.time()

# print("El gnomo tarda " + str(end - start))
