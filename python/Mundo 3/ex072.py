cont = ('zero', 'um', 'dois', 'tres', 'quatro', 
        'cinco','seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Informe um numero entre de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'voce digitou o número {cont[num]}')
