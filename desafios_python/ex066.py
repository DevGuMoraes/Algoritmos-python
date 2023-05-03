print('-'*20)
print('Sistema de soma')
print('-'*20)
tot = soma = 0
while True:
    num = int(input('Digite um valolr (999 para parar): '))
    if num == 999:
        break
    tot += 1
    soma += num
print(f'A soma de todos os {tot} valores foi {soma}!')
