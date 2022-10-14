from random import seed, randint
seed()

def matriz(n):
    m = []
    for termo1 in range(n):
        linha = []
        for termo2 in range(n):
            linha.append(randint(1, 100))

        m.append(linha)
    return m

def maior_menor(n):
    id_max = 0
    id_min = 0
    maior = 0
    menor = 999999999
    m2 = matriz(n)

    for linha in m2:
        for item in linha:
            if item > maior:
                maior = item
                id_max = (m2.index(linha), linha.index(item))
            if item < menor:
                menor = item
                id_min = (m2.index(linha), linha.index(item))
    return f'{id_max}, {id_min}'


def main():
    ordem = int(input().strip())
    print(maior_menor(ordem))

if __name__ == '__main__':
    main()
