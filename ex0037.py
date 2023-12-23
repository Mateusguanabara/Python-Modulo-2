num = int(input('Digite Um Número Inteiro?'))
print('''Escolha uma das Bases De Conversão:
[1] Binário
[2] Octal
[3]HexaDecimal''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} Convertido para Binário é igua á {}'.format(num,bin(num)))
elif opção == 2:
    print('{} Convertido para Octal é igual á {}'.format(num,oct(num)))
else:
    print('{} Conertido para HexaDecimal é igual á {}'.format(num , hex (num)))







