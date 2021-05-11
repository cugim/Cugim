palavras = ('Anus', 'Anus', 'Baba-ovo', 'Babaca', 'Bacura', 'Bagos',
            'Bebum', 'Besta', 'Biscate', 'Boazuda', 'Boceta', 'Boco')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
