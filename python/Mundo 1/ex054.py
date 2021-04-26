from datetime import date # pra saber a data do computer
atual = date.today().year # agora temas a data do computer
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa {}ª nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
       totmaior += 1
    else:
       totmenor += 1
print('O numero de pessoa menores de idade é  {}'.format(totmenor))
print('O numero de pessoas maiores de idade é {}'.format(totmaior))

        
