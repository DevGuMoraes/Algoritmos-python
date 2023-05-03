aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
for k, v in aluno.items():
    print(f'- {k}: {v}')
if aluno['Media'] >= 7.0:
    aluno['situação'] = 'Aprovado'
if 5.0 <= aluno['Media'] < 7.0:
    aluno['situação'] = 'Recuperação'
if aluno['Media'] < 5:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k}: {v}')