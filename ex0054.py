from datetime import date
atual = date.today().year
totmaior=0 #VARIVEL CONTADOOR
totmenor=0 #VARIVAL CONTADOR
for pess in range(1,8):
    nasc = int(input('Digite sua {}º Data De Nascimento??'.format(pess)))
    idade = atual - nasc #PARA DESCOBRIR A IDADE DA PESSOA !!!!
    if idade >= 21:
        totmaior += 1 #CONTADOR PARA ACRESCENTAR + 1 PESSOA MAIOR
    else:
        totmenor += 1 #CONTADOR PARA ACRESCENTAR +1 PESSOA MENOR
print('Ao todo tivemos {} Pessoas Maiores'.format(totmaior))
print('Tivemos {} Pessoas Menores De Idade'.format(totmenor))
