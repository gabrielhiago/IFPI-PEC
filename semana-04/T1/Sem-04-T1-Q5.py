def main():
    def dimensoes_sala(h, c, l):
        a_piso = l * c
        vol_sala = l * c * h
        a_paredes = (2 * h * l) + (2 * h * c)
        return a_piso, vol_sala, a_paredes
    altura = float(input().strip())
    comp = float(input().strip())
    largura = float(input().strip())
    area_piso, volume_sala, area_parede = dimensoes_sala(altura, comp,  largura)
    print(area_piso)
    print(volume_sala)
    print(area_parede)
if __name__ == '__main__':
    main()
