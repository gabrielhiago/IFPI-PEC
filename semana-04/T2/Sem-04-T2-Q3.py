def main():
    def porcentagem(preco, percentual):
        aumento = preco + (preco * (percentual / 100))
        desconto = preco - (preco * (percentual / 100))
        return aumento, desconto
    prec = float(input().strip())
    percent = float(input().strip())
    aum, desc = porcentagem(prec, percent)
    print(f'{aum:.2f}')
    print(f'{desc:.2f}')
if __name__ == '__main__':
    main()
