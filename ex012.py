preço = float(input('Preço original do produto: '))
desconto = preço * 0.05
preçofinal = preço - desconto
print('O seu produto de {}€ fica por {:.2f}€'.format(preço, preçofinal))
