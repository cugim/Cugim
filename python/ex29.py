vel = int(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Voce foi multado! OTARIO, o limite é 80km/h voce está a {}km/h'.format(vel))
else:
    print('Voce está dentro do limite, sua velocidade é de {}'.format(vel))    