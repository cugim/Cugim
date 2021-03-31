produto = float(input('Qual é o preço do produto? R$: '))
desconto = produto - (produto*5/100)
print('O pruduto que custava R${}, na promoção com desconto de 5% vai custar R%{:.2f}'.format(produto, desconto))
