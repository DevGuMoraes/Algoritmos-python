
# tirei os espaços antes e depois da frase, e AUMENTEI ela.
frase = str(input('escreva: ')).strip().upper()
palavras = frase.split()  # Fizemos uma lista com o Split().
junto = ''.join(palavras)  # Juntei tudo em um espaço só.
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):  # Aqui colocaquei da ultima letra até a primeira voltando uma letra
    inverso += junto[letra]  # depois testei se a frase é mesma, de traz para frente.'''''
print(junto, inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print('A frase capitada não é um palindromo')
