sal = float(input('Qual é o salário do Funcionário? R$ '))
novosal = sal + (sal*15/100)
print('Um funcionário qie ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(sal, novosal))
