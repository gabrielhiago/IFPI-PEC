def maximo(a, b):
    if a > b:
        maior = a
        return maior
    else:
        maior = b
        return maior

def minimo(a, b):
    if a < b:
        menor = a
        return menor
    else:
        menor = b
        return menor

def comparacao(a, b, c, d, e):
    maior, menor = maximo(a, b), minimo(a, b)
    maior, menor = maximo(maior, c), minimo(menor, c)
    maior, menor = maximo(maior, d), minimo(menor, d)
    maior, menor = maximo(maior, e), minimo(menor, e)
    return f'maior {maior}, menor {menor}'

n1 = int(input().strip())
n2 = int(input().strip())
n3 = int(input().strip())
n4 = int(input().strip())
n5 = int(input().strip())
print(comparacao(n1, n2, n3, n4, n5))
