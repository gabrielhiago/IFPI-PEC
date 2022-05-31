def main():
    def calcular(a, b, c):
        return (2 * a) + (5 * b) - c
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    resultado = calcular(num1, num2, num3)
    print(resultado)
if __name__ == '__main__':
    main()
