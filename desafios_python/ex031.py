km = float(input('Quantos Km percorridos na viagem? '))
if km <= 200:
    valor = 0.50 * km
else:
    valor = 0.45 * km
print('O valor da viagem com o total de {}Km ficou R${}'.format(km, valor))
