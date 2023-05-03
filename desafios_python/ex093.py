jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
for p in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {p}: ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'- O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(partidas):
    print(f'    => na partida {i}, fez {v} gols')
print(f'foi um total de {jogador["total"]} gols.')
              