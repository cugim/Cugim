from random import randint
r = randint(0,9)
ten = int(input('O computador pensou em um numero!! Tente acertar: '))
if ten == r:
    print('O numero ta certo {}'.format(ten))
else:
    print('O numero que digitou nao tem nada a ver!!')
    print(r)
    