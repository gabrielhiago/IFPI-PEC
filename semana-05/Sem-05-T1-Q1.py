def main():
    def cont_carac(nome):
        cont = len(nome)
        return f'{cont}'
    nom = input().strip()
    print(cont_carac(nom))
if __name__ == '__main__':
    main()
