alt = float(input('Altura atual: '))
peso = float(input('Peso atual: '))
imc = peso / (alt ** 2)
print('Seu IMC é {:.1f} e voce está:'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('sobre o peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
else:
    print('Valor inválido')
