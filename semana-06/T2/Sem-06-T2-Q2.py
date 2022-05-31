def verifica_letra(letra):
    return letra.isalpha()

def main():
    carac = input().strip()
    print(verifica_letra(carac))

if __name__ == '__main__':
    main()
