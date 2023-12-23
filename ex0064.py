n = cont = soma = 0
n = int(input('Digite um número , [999 e para parar]:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número , [999 e para parar]:'))
print('Você digitou {} Valores é a soma entre eles {}'.format(cont,soma))




