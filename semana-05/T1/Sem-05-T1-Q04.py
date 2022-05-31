def main():
    def maximo_minimo_media(a, b, c, d, e):
        maior = max(a, b, c, d, e)
        menor = min(a, b, c, d, e)
        media = (a + b + c + d + e) / 5
        return maior, menor, media
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    num4 = int(input().strip())
    num5 = int(input().strip())
    maior, menor, media = maximo_minimo_media(num1, num2, num3, num4, num5)
    print(f'{maior}\n{menor}\n{media}')
if __name__ == '__main__':
    main()
