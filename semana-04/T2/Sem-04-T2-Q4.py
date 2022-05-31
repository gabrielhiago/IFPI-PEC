def main():
    def conversor_minutos(min):
        h = min // 60
        m = min % 60
        return h, m
    tot_min = int(input().strip())
    hora, minutos = conversor_minutos(tot_min)
    print(f'{hora}:{minutos}')
if __name__ == '__main__':
    main()
