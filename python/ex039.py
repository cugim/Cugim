from datetime import  date
atual = date.today().year
sexo = str(input('Informe M para masculino e F para feminino: '))
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
if sexo == 'F':
    print('Você não prescisa se alistar')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já devia ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
