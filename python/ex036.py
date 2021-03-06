casa = float(input('Qual o valor da casa? '))
sal = float(input('Informe seu salário R$:  '))
anos = int(input('Em quantos anos voce pretende pagar? '))
prestação = casa / (anos * 12)
minimo = sal * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('\033[0;31;40mEmprestimo APROVADO :D\033[m')
else:
    print('\033[0;31;40mEmprestimo NEGADO :C\033[m')


