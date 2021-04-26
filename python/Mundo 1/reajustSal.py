sal = float(input('Informe seu salário R$: '))
novoSal = sal + (sal*15/100)
print('Seu salario era de R${:.2f}, com 15% de aumento foi para R${:.2f}'.format(sal,novoSal))
