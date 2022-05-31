def verifica(carac):
    return carac.isalpha() or carac.isnumeric() and carac in ('0, 1, 2, 3, 4, 5, 6, 7, 8, 9')

def main():
    caractere = input().strip()
    print(verifica(caractere))

if __name__ == '__main__':
    main()
