def main():
    def tempo_segundos(h, m, s):
        return (h * 3600) + (m * 60) + s
    hora = int(input().strip())
    min = int(input().strip())
    seg = int(input().strip())
    tot_seg = tempo_segundos(hora, min, seg)
    print(tot_seg)
if __name__ == '__main__':
    main()
