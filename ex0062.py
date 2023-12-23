print('-='*7)
print('Gerador de PA:')
print('-='*7)
primeiro = int(input('Digite a primeira PA:'))
razão = int(input('Digite a razão :'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo),end= '')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você deseja digitar a mais:'))
print('Fim')
print('Progressão Finalizada com {} Progressões'.format(total))


