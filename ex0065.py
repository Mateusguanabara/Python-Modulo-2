mediadogrupo = 0
resp = 'Ss'
maior = menor = quant = soma = 0
while resp in 'Ss':
    núm = int(input('Digite um valor?'))
    soma += núm
    quant += 1
    mediadogrupo = soma / quant
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Você Deseja continuar:[S,N]')).upper()
print('Foram digitados {} Números é a média do grupo totaliza {}'.format(quant,mediadogrupo))
print('Soma dos valores é {}'.format(soma))
print('O maior valor foi {} é o menor valor foi {}'.format(maior,menor))







