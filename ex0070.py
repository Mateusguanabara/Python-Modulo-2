maior = cont = total = menor = 0
barato = ''
print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)
while True:
    produto = str(input('Nome do produto:'))
    preço = int(input('Valor:R$'))
    continuar = str(input('Quer continuar? [S/N]')).upper()
    total += preço
    cont += 1
    if preço >= 1000:
        maior += 1
    if cont == 1 or preço < menor:
       menor = preço
       barato = produto
    if continuar =='N':
        break
print('=== FIM DO PROGRAMA ===')
print(f'{maior} produtos custam mais de R$ 1,000 ')
print(f'Ao todo o valor das compras ficou R$ {total}')
print(f'Dessas compras {barato} é o mais barato saindo por R${menor :.2f}')