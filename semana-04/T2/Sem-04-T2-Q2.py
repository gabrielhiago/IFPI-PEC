def main():
    def dimensoes_quadrado(l):
        area = l ** 2
        perimetro = l + l + l + l
        return area, perimetro
    lado = float(input().strip())
    a_quadrado, p_quadrado = dimensoes_quadrado(lado)
    print('%4.4f' % a_quadrado)
    print('%4.4f' % p_quadrado)
if __name__ == '__main__':
    main()
