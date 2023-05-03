print('Tabuada 3.0')
count = 0
while True:
    print('=-='*13)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('=-='*13)
    if num < 0:
        break
    for count in range(0, 10):
        print(f'{num} x {count} = {num*count}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
