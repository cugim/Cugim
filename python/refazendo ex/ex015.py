dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias*60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

'Eu sabia mas achei que tava errado, bem no fim a minha primeira lógica tava certa!'