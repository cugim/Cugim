soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos numeros inteiros dá {}'.format(soma))