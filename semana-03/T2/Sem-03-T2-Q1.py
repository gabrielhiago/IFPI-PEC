raio = float(input())
PI = 3.141592
comp = 2 * PI * raio
areacirc = PI * (raio ** 2)
areaesf = 4 * PI * (raio ** 2)
volesf = 4 / 3 * PI * (raio ** 3)
print('{:.6f}'.format(comp))
print('{:.6f}'.format(areacirc))
print('{:.6f}'.format(areaesf))
print('{:.6f}'.format(volesf))
