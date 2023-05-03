lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMAR', 'FUTURO')
for palavra in lista:
    print(f'Na palavra {palavra:<3} temos', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra.lower():>2}', end=' ')
    print()