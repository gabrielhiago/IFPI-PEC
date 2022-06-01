def ordem(a, b, c):
    if max(a, b, c) == a and min(a, b, c) == b:
        primeiro, segundo, terceiro = b, c, a
        return f'{primeiro}, {segundo}, {terceiro}'
    elif max(a, b, c) == b and min(a, b, c) == c:
        primeiro, segundo, terceiro = c, a, b
        return f'{primeiro}, {segundo}, {terceiro}'
    elif max(a, b, c) == c and min(a, b, c) == a:
        primeiro, segundo, terceiro = a, b, c
        return f'{primeiro}, {segundo}, {terceiro}'
    else:
        return f'dados incorretos'

def main():
    n1 = float(input('Informe o 1º valor: ').strip())
    n2 = float(input('Informe o 2º valor: ').strip())
    n3 = float(input('Informe o 3º valor: ').strip())
    print(ordem(n1, n2, n3))

if __name__ == '__main__':
    main()