from os import closerange
from time import sleep
n1 = int(input('Priemiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção  == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação de {} e {} da {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:  
            maior   = n2
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else: 
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa! Volte sempre')
