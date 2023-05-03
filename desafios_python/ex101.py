def voto(nasc):
     from datetime import date
     atual = date.today().year
     idade = atual - nasc
     if idade < 16:
          return f'Com {idade} anos: VOTO NEGADO'
     elif 18 <= idade <= 70:
          return f'Com {idade} anos: VOTO OBRIGATÓRIO'
     else:
          return f'Com {idade} anos: VOTO NEGADO'


anonasc = int(input('Em que ano você nasceu?  '))
print(voto(anonasc))
