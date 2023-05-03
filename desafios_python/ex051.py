print('=-='*12)
print('Progressaão Aritmética')
print('=-='*12)
primeiro = int(input('Digite o termo inicial da PA:'))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')