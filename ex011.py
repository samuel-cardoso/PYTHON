altura = float(input('Altura da Parede: '))
largura = float(input('Largura da Parede: '))
area = altura * largura
litros = area / 2
print('A sua parede tem {} m² e precisa de {:.2f} litros de tinta!'.format(area, litros))