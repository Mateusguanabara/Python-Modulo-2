frase = str(input('Digite uma frase?')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = '' #CONTADOR
inverso = junto[::-1] #FATIAMENTO
'''for letra in range(len(junto)-1,-1,-1): 
    inverso += junto[letra]''' #CORTANDO O FOR
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('\033[42:30m Frase é um PALÍNDROMO!\033[m')
else:
    print('\033[31m NÃO É UM PALÍNDROMO!\033[m')

