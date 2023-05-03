vel = int(input('Valocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Ao exceder o limite de velocidade a {} Km/h'.format(vel))
    print('Sua multa foi de R${}'.format(multa))
else:
    print('Velocidade adequada. Tenha conciencia no trânsito. ')