preço = float(input('Informe o valor do produto: R$ '))
novo = preço - (preço*5/100)
print('O produto que custava {:.2f}, na promoção vai custar {:.2f}'.format(preço,novo))
