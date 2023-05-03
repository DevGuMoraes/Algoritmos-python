alt = float(input('Altura: '))
larg = float(input('Largura: '))
area = alt * larg
tinta = area / 2
print('Para pintar uma área de \{}m² você precisará de \033[4:32m{:.2f}L\033[m de tinta'.format(area, tinta))
