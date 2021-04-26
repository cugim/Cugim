sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0].strip()
print('Sexo {} registrador com sucesso'.format(sexo))
