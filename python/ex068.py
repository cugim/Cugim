print('-='*10)
print('Vamos jogar par ou impar')
print('-='*10)
n  = 0
while True:
    if n == 999:
        break
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar[P/I]: ')).upper()
    print('-'*10)
    if escolha == 'P':
        if (n%2) == 0:
            n += 2
