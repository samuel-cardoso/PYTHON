dias = int(input('Por quantos dias teve com o carro: '))
km = float(input('Quanto km fez: '))
pagar = (dias * 60) + (km * 0.15)
print('O total a pagar é de {}€'.format(pagar))
