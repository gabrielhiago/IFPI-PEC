def conversao_kelvin(temp, esc):
    if esc == 'K':
        return temp
    if esc == 'C':
        return temp + 273
    if esc == 'F':
        return round((((temp - 32) * (5 / 9)) + 273), 2)

def nome_mes(id):
    if id == 0:
        return 'Janeiro'
    if id == 1:
        return 'Fevereiro'
    if id == 2:
        return 'Março'
    if id == 3:
        return 'Abril'
    if id == 4:
        return 'Maio'
    if id == 5:
        return 'Junho'
    if id == 6:
        return 'Julho'
    if id == 7:
        return 'Agosto'
    if id == 8:
        return 'Setembro'
    if id == 9:
        return 'Outubro'
    if id == 10:
        return 'Novembro'
    if id == 11:
        return 'Dezembro'

def main():
    temperaturas = []
    soma = 0

    for item in range(12):
        temperatura = int(input().strip())
        escala = input().strip().upper()[0]

        t_kelvin = conversao_kelvin(temperatura, escala)
        temperaturas.append(t_kelvin)
        soma += t_kelvin

    media = soma / len(temperaturas)

    print('TEMPERATURA MÉDIA ANUAL')
    print(f'{round(media, 2)}K')

    print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
    for i in range(12):
        if temperaturas[i] > media:
            print(f'{nome_mes(i)}: {round(temperaturas[i], 2)}K')

if __name__ == '__main__':
    main()
