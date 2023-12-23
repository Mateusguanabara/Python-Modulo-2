núm=(int(input('Digite um número?')))
tot=0
for c in range(1,núm +1):
    if núm % c == 0:
        print('\033[34m',end='')
        tot+=1
    else:
        print('\033[m',end='')
    print('{}'.format(c), end=' ')
print('\n\033[35m O número {} Foi Dividio {} Vezes\033[m'.format(núm,tot))
if tot == 2:
     print('É UM NÚMERO PRIMO!!')
else:
     print('ELE NÃO E CONSIDERADO NÚMERO PRIMO!!')