resp = 'S'
soma = quant = media = maior = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num 
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
media = soma / quant
print('Voce digitou {} numero e a media foi {}'.format(quant, media))
print('O maior valor foi {} e  menor foi {}'.format(maior, menor))
