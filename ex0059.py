from time import sleep
valor1 = int(input('Digite o 1° valor?'))
valor2 = int(input('Digite o 2 ° valor?'))
opção = 0
while opção != 5:
    print('''Escolha Uma Das Opçoes Abaixo:
            [1]Soma
            [2]Multiplicar
            [3]Maior
            [4]Novos Números
            [5]Sair Do Pograma''')
    opção = int(input('Qual Sua Opção??'))
    if opção == 1:
        soma = valor1 + valor2
        print('Valor de {} + {} = {}'.format(valor1,valor2,soma))
    if opção == 2:
        produto = valor1 * valor2
        print('Valor de {} X {} = {}'.format(valor1,valor2,produto))
    if opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Valor {} é {} Maior é {}'.format(valor1,valor2,maior))
    if opção == 4:
        valor1 = int(input('Digite novamente o 1° Valor?'))
        valor2 = int(input('Digite o 2° Valor ?'))
if opção == 5:
 print('Você encerrou o programa...')
sleep(1)
print('Volte sempre!')






