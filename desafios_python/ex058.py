from random import randint
palpites = 1
computador = randint(0, 10)
print('''HAHAHA Sou seu computador e estou aqui para te desafiar!!
Pensei em um numero de 0 a 10... 
Vamos ver se voce terá capacidade para acertar!''')
jogador = int(input('Digite um valor de 0 a 10: '))
acertou = False
while not acertou:
    palpites += 1
    jogador = int(input('Digite um valor de 0 a 10: '))
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('Hmmm... Talvez um palpite MENOR.')
        n = int(input('Seu palpite: '))
    else:
        print('Talvez um palpite MAIOR...')
        n = int(input('Seu palpite: '))
if palpites < 5:
    print('NÃÃÃO!! VOCÊ VENCEU!! Precisou de apenas {} palpites. '.format(palpites))
elif palpites > 5:
    print('HORRIVEL! FINALMENTE ACERTOU, Mas precisou de {} palpites, TREINE MAIS.'.format(palpites))
