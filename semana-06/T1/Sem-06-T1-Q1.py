def saudacao():
    nome = str(input().strip())
    sexo = int(input().strip())
    if sexo == 1:
        print('Ilmo Sr. {}'.format(nome))
    else:
        print(f'Ilma Sra. {nome}')
def main():
    saudacao()
if __name__ == '__main__':
    main()