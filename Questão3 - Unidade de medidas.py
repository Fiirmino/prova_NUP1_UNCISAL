# UNIDADE DE MEDIDAS
uni = input('\033[1:4:33:40mDigite a unidade desejada (km/hm/dam/dm/cm/mm):\033[m ').strip()
unidade_medida = uni.upper() #deixa tudo em 'uni' maiúsculo para n dar pau !!
valor = int(input('\033[1:4:33:40mDigite o valor desejado a ser convertido em metros:\033[m '))
if uni == 'km':
    print(f'{valor:.0f}m = {valor*0.001}Km')
elif uni == 'hm':
    print(f'{valor:.0f}m = {valor * 0.01}hm')
elif uni == 'dam':
    print(f'{valor:.0f}m = {valor * 0.1} decâmetros')
elif uni == 'dm':
    print(f'{valor:.0f}m = {valor * 10} decímetros')
elif uni == 'cm':
    print(f'{valor:.0f}m = {valor * 100} centímetros')
elif uni == 'mm':
    print(f'{valor:.0f}m = {valor * 1000} milímetros')
else:
    print('\033[1:4:31mErro no programa, selecione novamente uma medida válida !!!\033[m')
