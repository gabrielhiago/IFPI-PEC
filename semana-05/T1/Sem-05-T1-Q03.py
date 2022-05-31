def main():
    def duracao(ts):
        h = ts // 3600
        m = (ts % 3600) // 60
        s = (ts % 3600) % 60
        return f'{h}:{m}:{s}'
    tempo = int(input().strip())
    print(duracao(tempo))
if __name__ == '__main__':
    main()
