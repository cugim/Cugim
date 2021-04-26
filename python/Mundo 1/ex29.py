vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('Voce foi multado! OTARIO, o limite é 80km/h voce está a {}km/h'.format(vel))
    multa = (vel-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
