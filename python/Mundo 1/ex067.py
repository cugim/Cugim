n = c = 0 
while True:
    print('Numeros negativos encerra o programa!!!!')
    n = int(input('quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range (1, 11):
        print('{} X {} = {}'.format(n ,c, n*c))
    print('-'*30)
print('PROGRAMA ENCERRADO. volte sempre!')
print('-'*30)    

