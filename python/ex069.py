print('-'*10)
print('CADASTRE UMA PESSOA')
print('-'*10)
resp = ''
sm = sf = maior = menor20 =0
while resp in 'S':
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-'*10)
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        sm += 1
    if sexo == 'F' and idade < 20:
        menor20 += 1
    elif sexo == 'F':
        sf += 1
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp !='S':
        break 
print('-'*10)
print(f'O total de pessoas com mais de 18 são {maior}')
print(f'Ao todo temos {sm} homens cadastrados')
print(f'Ao todo temos {menor20} mulheres cadastradas com menos de 20')
