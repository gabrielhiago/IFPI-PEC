def main():
    def inversor_numeros(num):
        m = num // 1000
        c = (num % 1000) // 100
        d = ((num % 1000) % 100) // 10
        u = ((num % 1000) % 100) % 10
        invertido = (u * 1000) + (d * 100) + (c * 10) + (m * 1)
        return invertido
    numero = int(input().strip())
    n_invert = inversor_numeros(numero)
    print(n_invert)
if __name__ == '__main__':
    main()
