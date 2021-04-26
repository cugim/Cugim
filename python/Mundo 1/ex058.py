from time import sleep
from random import randint
computador = randint(0, 10)
print('Sou seu compiuter... Acabei de pensar em um número entre 0 e 10.')
print('Srá que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('O numero que pensei foi...')
sleep(1)
print(computador)
print('Acertou com {} tentativas. Parabéns!'.format(palpites))

