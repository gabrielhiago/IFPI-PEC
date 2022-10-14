from random import seed, randint
seed()

def matriz(linhas, colunas):
    m = []

    for l in range(linhas):
        lin = []
        for c in range(colunas):
            lin.append(randint(0, 100))
        m.append(lin)

    return m

def soma_primeira_linha(matriz):
    return sum(matriz[0])

def soma_ultima_coluna(matriz):
    soma = 0

    for linha in matriz:
        soma += linha[-1]
    return soma

def media(matriz):
    soma = 0
    qtd = 0

    for linha in matriz:
        soma += sum(linha)
        qtd += len(linha)

    return round((soma / qtd), 2)

def menor_valor(matriz):
    menor = 99999999

    for linha in matriz:
        for termo in linha:
            if termo < menor:
                menor = termo
    return menor

def maior_valor(matriz):
    maior = 0

    for linha in matriz:
        for termo in linha:
            if termo > maior:
                maior = termo
    return maior

def main():
    n_linhas = int(input('numero de linhas: ').strip())
    n_colunas = int(input('numero de colunas: ').strip())

    M = matriz(n_linhas, n_colunas)
    tr = (soma_primeira_linha(M), soma_ultima_coluna(M), media(M), menor_valor(M), maior_valor(M))
    print(M)
    print(tr)
    '''print(soma_primeira_linha(M))
    print(soma_ultima_coluna(M))
    print(media(M))
    print(menor_maior(M))'''

if __name__ == '__main__':
    main()
