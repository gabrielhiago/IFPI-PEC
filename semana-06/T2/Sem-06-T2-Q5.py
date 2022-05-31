def e_vogal(carac):
    return carac in ('a, e, i, o, u, A, E, I, O, U')

def e_consoante(carac):
    return carac.isalpha() and carac not in ('a, e, i, o, u, A, E, I, O, U')

def e_numero(carac):
    return carac.isnumeric()

def main():
    caractere = input().strip()
    if caractere not in ('ç, Ç,  , á, Á, é, É, í, Í, Ó, ó, ú, Ú, ã, õ, Ã, Õ, ê, Ê, à, À'):
        if e_vogal(caractere):
            print('vogal')
        elif e_consoante(caractere):
            print('consoante')
        elif e_numero(caractere):
            print('número')
        else:
            print('símbolo')
    else:
        print('símbolo')

if __name__ == '__main__':
    main()
