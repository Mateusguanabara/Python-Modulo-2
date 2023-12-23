maiorpeso=0
menorpeso=0
for p in range(1,6):
    peso = float(input('Informe Seu {}º Peso?'.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O Maior Peso Lido Foi {}KG'.format(maiorpeso))
print('O Menor Peso Lido Foi {}KG'.format(menorpeso))










