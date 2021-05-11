
numeros = (int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')),
          int(input('Digite um numero: ')))
print(f'Você digitou os {numeros}')
print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 nao se encontra em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
     if n % 2 == 0:
        print(n, end=' ')
