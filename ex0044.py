print('{:=^40}'.format(' LOJAS MIRANDA '))
preço = float(input('Digite O Valor Total Das Compras??'))
print('''
[1] À vista Dinheiro/Cheque
[2] À vista no Cartão
[3] 2x No Cartão
[4] 3x Ou Mais No Cartão''')
opção = int(input('Qual é a opção??'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua Compra Será Parcelada em 2x De R${:.2f} SEM JUROS!'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas Parcelas Deseja? '))
    parcela = total / totparc
    print('Sua Compra Será Parcelada em {}x De R${:.2f} COM JUROS!'.format(totparc,parcela,))
else:
    total = 0
    print('\033[2;31m OPÇÃO INVÁLIDADE DE PAGAMENTO , Tente Novamente!!\033[m')
print('Sua Compra De R${:.0f} Custará No Final R${:.2f}'.format(preço,total))
