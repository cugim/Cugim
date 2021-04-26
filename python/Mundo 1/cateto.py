import math
co = float(input('complemento do catero oposto: '))
ca = float(input('complemento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
