numero = int(input('Me diga um nuemro qualquer: '))
resultado = numero % 2
print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))
    