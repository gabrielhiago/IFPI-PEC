def data(d1, m1, a1, d2, m2, a2):
    if a1 > a2 or m1 > m2 or d1 > d2:
        return f'a data {d1}/{m1}/{a1} é a mais recente'
    elif a2 > a1 or m2 > m1 or d2 > d1:
        return f'a data {d2}/{m2}/{a2} é a mais recente'
    else:
        return f'As duas datas são iguais'

def main():
    dia1 = int(input().strip())
    mes1 = int(input().strip())
    ano1 = int(input().strip())
    dia2 = int(input().strip())
    mes2 = int(input().strip())
    ano2 = int(input().strip())
    print(data(dia1, mes1, ano1, dia2, mes2, ano2))

if __name__ == '__main__':
    main()