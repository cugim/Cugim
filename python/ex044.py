print('{:=^40}'.format(' LOJINHA DO RAFÂO '))
compras = float(input('Informe o valor das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    desconto = compras - (compras*10/100)
    print('A sua compra de {} recebeu um desconto de 10% e foi para {}'.format(compras, desconto))
elif opção == 2:
    desconto = compras - (compras*5/100)
    print('A sua compra de {} recebeu um desconto de 5% e foi para {}'.format(compras, desconto))
elif opção == 3:
    total = compras
    parcela = compras / 2
    print('Voce optou por parcelar e sua compra será 2X de {:.2f}R$'.format(parcela))
    print('Sua compra de {} vai custar {} no final'.format(compras, total))
elif opção == 4:
    juros = compras + (compras * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = juros / totalparc
    print('Sua compra será parcela em {}X de {:.2f}R$ COM JUROS!'.format(totalparc, parcela))
    print('A sua compra de {} vai acabar custando {}'.format(compras, juros))
else: 
    print('OPÇÂO INVALIDA DE PAGAMENTO')
