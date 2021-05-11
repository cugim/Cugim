listagem = ('Lápis', 1.75,
            'Borracha', 50,
            'Caderno', 5.50,
            'Livro', 1.90,
            'Estojo', 3.70,
            'Compasso', 1.50,
            'Mochila', 120.22,
            'Caneta', 22.30,
            'Transferidor', 4.20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:.>7.2f}')
print('-' * 40)
        