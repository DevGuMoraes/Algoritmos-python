print('TABELA BRASILEIRAO')
print('=-=' * 40)
tabela = ('Santos', 'Atlético', 'Corinthians', 'Avaí', 'Cuiabá', 'Internacional', 'Bragantino',
          'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminense', 'America',
          'Ceara SC', 'Atlético-PR', 'Atlético-GO', 'Juventude', 'Goías', 'Fortaleza')
print(f'os primeiros 5 colocados foram: {tabela[:5]}')
print('=-=' * 40)
print(f'Os ultimos 5 colocados foram: {tabela[-5:]}')
print('=-=' * 40)
print(sorted(tabela))
if 'Chapecoense' not in tabela:
    print('Chapecoense não se classificou para o Brasileirão deste ano.')
else:
    print(tabela.index('Chapecoense'))


