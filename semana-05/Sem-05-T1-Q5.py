def main():
    def pagamento(compra):
        a_vista = compra - (compra * (9 / 100))
        cinco_vzs = compra / 5
        dez_vzs = (compra + (compra * 17 / 100)) / 10
        return f'{a_vista:.2f}\n{cinco_vzs:.2f}\n{dez_vzs:.2f}'
    valor = float(input().strip())
    print(pagamento(valor))
if __name__ == '__main__':
    main()
