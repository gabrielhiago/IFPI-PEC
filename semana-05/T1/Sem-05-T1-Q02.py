def main():
    def codigo_carac(digito):
        cod = ord(digito)
        return f'{cod}'
    caractere = input().strip()
    print(codigo_carac(caractere))
if __name__ == '__main__':
    main()
