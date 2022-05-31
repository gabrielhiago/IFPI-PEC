def e_consoante(letra):
    return letra.isalpha() and letra not in ('a, e, i, o, u, A, E, I, O, U')

def main():
    carac = str(input().strip())
    print(e_consoante(carac))

if __name__ == '__main__':
    main()
