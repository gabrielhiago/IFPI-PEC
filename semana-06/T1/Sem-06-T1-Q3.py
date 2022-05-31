def sinal():
    cor = input().strip()
    if cor.upper() == 'V':
        return 'Siga'
    elif cor.upper() == 'A':
        return 'Atenção'
    else:
        return 'Pare'
def main():
    print(sinal())
if __name__ == '__main__':
    main()
