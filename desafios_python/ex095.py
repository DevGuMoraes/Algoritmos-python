jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, tot):
        partidas.append(int(input(f'Quantos gols  na partida {p}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apensa S ou N.')
    if resp in 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end= '')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de que jogador? (999 Interrompe) '))
    print('-' * 40)
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        print('-' * 40)
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    Na partida {i + 1} ele fez {g} gols.')
print('<< VOLTE SEMPRE >>')
