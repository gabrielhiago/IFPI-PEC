def media(a, b, c, d, e):
    media = (a + b + c + d + e) / 5
    if a > media:
        print(f'{a:.2f}')
    if b > media:
        print(f'{b:.2f}')
    if c > media:
        print(f'{c:.2f}')
    if d > media:
        print(f'{d:.2f}')
    if e > media:
        print(f'{e:.2f}')
    print(f'{media:.2f}')

def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    n4 = int(input().strip())
    n5 = int(input().strip())
    print(media(n1, n2, n3, n4, n5))

if __name__ == '__main__':
    main()
