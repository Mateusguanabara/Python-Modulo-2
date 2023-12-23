pt=int(input('Digite um 1° Termo De Uma Progressão Artimetica?'))
r=int(input('Digite uma Razão De Uma PA?'))
decimo = pt + (10-1)*r
for c in range(pt,decimo + r ,r):
 print('{}'.format(c), end='-> ')
print('ACABOU')