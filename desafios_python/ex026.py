frase = str(input('Digite uma frase: ')).upper().strip()
print('QUantas vezes aparece a Letra A? {}'.format(frase.count('A')))
print('A primeira posição dele: {}'.format(frase.find('A')+1))
print('A aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))
