#for t in times:
    #print(t)
 
times = ('Flamengo', 'Corinthians', 'São Paulo', 'Atlético/MG',
         'Internacional', 'Ceará', 'Bahia', 'Athletico/PR',
         'Chapecoense', 'Cuiabá', 'Fluminense', 'Palmeiras',
         'Santos', 'América/MG', 'Grêmio', 'Fortaleza', 'Sport',
         'RB Bragantino', 'Juventude', 'Atlético/GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')