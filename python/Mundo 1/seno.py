from math import radians, sin, cos, tan
an = float(input('Digite o angulo que voce deseja:'))
seno = sin(radians(an))
print('O angulo {} tem o seno de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O angulo {} tem a tangente de {:.2f}'.format(an, tangente))
