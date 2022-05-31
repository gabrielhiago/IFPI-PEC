def main ():
    def media (a, b, c):
        m = (a + b + c) / 3
        return m
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    m = media(num1, num2, num3)
    print(m)
if __name__ == '__main__':
    main()
