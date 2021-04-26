n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
nota = (n1 + n2) / 2
if  7 > nota >= 5:
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, nota))
    print('o aluno está de RECUPERAÇÂO :D')
elif nota < 5:
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1 , n2, nota))
    print('O aluno está REPROVADO')
elif nota >= 7:
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1 , n2, nota))
    print('O aluno está APROVADO')
