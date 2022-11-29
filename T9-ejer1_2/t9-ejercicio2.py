from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def numImpar(x):
    if x % 2:
        return True

    return False

resultado = filter(numImpar, numeros)
print(list(resultado))

def suma(a, b):
    return a + b

res = reduce(suma, [1, 3, 5, 7, 9, 11, 13, 15])
print(res)

