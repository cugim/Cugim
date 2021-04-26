lar=float(input('Largura da parede: '))
alt = float(input('Altira da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(lar,alt,area))
tinta = area/2
print('Para printar essa parede voce precisará de {}l de tinta'.format(tinta))