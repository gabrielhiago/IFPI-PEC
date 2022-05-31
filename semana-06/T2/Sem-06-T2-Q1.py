def e_vogal(letra):
    return letra in ('a, e, i, o, u, A, E, I, O, U')

def main():
    carac = input().strip()
    print(e_vogal(carac))

if __name__ == '__main__':
    main()
