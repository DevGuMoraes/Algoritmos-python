temp = []
princ = []
mai = men = maip = menp = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = ' '
    if r not in 'SN':
        r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'Os dados foram {princ}')
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')