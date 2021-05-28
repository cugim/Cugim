#num = [2, 5, 9, 1]
#res = int(input('Informa um ae: '))
#num[0] = res
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#if res in num:
    #num.remove(res)
    #print(f'O valor removido foi {res}')
#else:
    #print('Não achei o numero')
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')