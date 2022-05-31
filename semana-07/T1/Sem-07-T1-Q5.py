def imc(h, p):
    IMC = p / (h ** 2)
    return IMC

def main():
    altura = float(input().strip())
    peso = float(input().strip())
    IMC = imc(altura, peso)
    if IMC < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= IMC < 25:
        print('Peso normal')
    elif 25 <= IMC < 30:
        print('Sobrepeso')
    elif 30 <= IMC < 35:
        print('Obeso Leve')
    elif 35 <= IMC < 40:
        print('Obeso Moderado')
    else:
        print('Obeso Mórbido')

if __name__ == '__main__':
    main()