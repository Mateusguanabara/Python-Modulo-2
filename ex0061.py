print('-='*7)
print('Gerador de PA:')
print('-='*7)
primeiro = int(input('Digite a primeira PA:'))
razão = int(input('Digite a razão :'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo),end= '')
    termo += razão
    cont += 1
print('FIM')
