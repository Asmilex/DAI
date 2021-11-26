def criba(n):
    primos = [True for i in range (n+1)]
    p = 2

    while p*p <= n:
        if (primos[p] == True):
            for i in range(p*p, n+1, p):
                primos[i] = False
        p += 1

    salida = []
    for p in range(2, n+1):
        if primos[p]:
            salida.append(p)

    return salida
