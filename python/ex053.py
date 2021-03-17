frase = str(input('Digite uma frase: ')).strip().upper() #leu a frase, eliminando espaços antes e depois
palavras = frase.split() #Slitou == Geral uma lista 
junto = ''.join(palavras) # juntou a lista
inverso = junto[::-1] # outra maneira de fazer sem o for
'''for letra in range(len(junto) - 1, -1, -1): # foi da ultima letra ate a primeira voltado uma letra
    inverso += junto[letra] # fez a frease ficar ao inverso'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:  # testou pra ver se os dois batiam
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
