def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

f = open("./numero_de_fibo.txt", "r")
n = int(f.read())
f.close()

f = open("./fibo.txt", "a")
f.write(str(fibonacci(n)))
f.close()
