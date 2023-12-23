print('\033[33m--\033[m'*15)
print('\033[2;37mSegmento De Reta , Reforçado!\033[m')
print('\033[33m--\033[m'*15)
r1 = float(input('Digite o 1º Segmento?'))
r2 = float(input('Digite o 2 º Segmento?'))
r3 = float(input('Digite o 3 º Segmento?'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos Acima Podem Formar Um Triângulo,')
if r1 == r2 == r3:
    print('O Segmento Acima Tem todos os Lados Iguais, \033[33mEQUILÁTERO !\033[m')
elif r1 == r2 == r3 == r1:
    print('Porém 2 Lados São Iguais é 1 Diferente , \033[34m ESCALENO  !\033[m')
else:
    print('Todos os Lados Diferentes ,\033[34m ISÓSCELES !!\033[m ')






