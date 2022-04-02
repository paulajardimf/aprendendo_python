times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
#print(f'Lista de times {times}')
#for t in times:
#    print(t)
print(f'Cinco primeiros times do Brasileirão: {times[0:5]}')
print(f'Quatro últimos times do Brasileirão: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'Posição do Chapecoense: {times.index("Chapecoense")+1}ª posição')
