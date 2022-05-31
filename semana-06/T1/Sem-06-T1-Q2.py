def eh_par(num):
    return num % 2 != 0
def main():
    numero = float(input().strip())
    print(eh_par(numero))
if __name__ == '__main__':
    main()
