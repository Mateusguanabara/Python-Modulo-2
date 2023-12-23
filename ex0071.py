print('='*30)
print('{:^30}'.format('BANCO MIRANDA'))
print('='*30)
valor = int(input('Qual valor você quer sacar?R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
       total -= céd
       totcéd += 1
    else:
        if totcéd > 0:
            print(f'Você sacou \033[4;31m {totcéd} \033[m Cédulas de \033[33m R${céd} \033[m')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
         break
print('-'*40)
print('Obrigado pela preferência Do BANCO MIRANDA ! Volte Sempre..')
print('Tenha um ótimo dia!')


